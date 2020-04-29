from . import __version__

import asyncio
import json
import aiohttp
import asyncio
import encodings.idna  # could be required with some versions of Python


class Bot:
    def __init__(
        self,
        token,
        *,
        user=False,
        listeners=None,
        proxy=None,
        user_agent=f"DiscordBot (https://github.com/Th0rgal/lightdiscord, {__version__})",
    ):
        self.token = token if user else f"Bot {token}"
        self.listeners = listeners
        self.proxy = proxy
        self.user_agent = user_agent

    async def start(self):
        response = await self._api_call("/gateway")
        await self._start(response["url"])

    async def handle_event(self, data):
        self.last_sequence = data["s"]
        event_name = data["t"]
        if self.listeners:
            for listener_name in self.listeners:
                if listener_name == event_name:
                    await self.listeners[listener_name](self, data)

    async def get_private_channel_id(self, recipient_id):
        return await self._api_call(
            "/users/@me/channels", "POST", json={"recipient_id": recipient_id}
        )

    async def send_message(self, channel_id, content):
        return await self._api_call(
            f"/channels/{channel_id}/messages", "POST", json={"content": content}
        )

    async def send_friend_request(self, username, discriminator):
        await self._api_call(
            "/users/@me/relationships",
            "POST",
            json={"discriminator": discriminator, "username": username},
        )

    async def sleep_typing(self, channel_id, delay):
        for _ in range(int(delay / 8)):
            await self.send_typing(channel_id)
            await asyncio.sleep(8)
        await self.send_typing(channel_id)
        await asyncio.sleep(delay % 8)

    async def send_typing(self, channel_id):
        await self._api_call(f"/channels/{channel_id}/typing", "POST", json={})

    async def _api_call(self, path, method="GET", **kwargs):
        # return the JSON body of a call to Discord REST API
        defaults = {
            "headers": {"Authorization": self.token, "User-Agent": self.user_agent}
        }
        kwargs = dict(defaults, **kwargs)
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                f"https://discordapp.com/api/v6{path}",
                proxy=self.proxy,
                **kwargs,
            ) as response:
                assert response.status >= 200 and response.status < 300, response.reason
                if response.status != 204:
                    return await response.json()

    async def _heartbeat(self, ws, interval):
        # send every interval ms the heatbeat message
        while True:
            await asyncio.sleep(interval / 1000)  # seconds
            await ws.send_json({"op": 1, "d": self.last_sequence})  # Heartbeat

    async def _start(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(
                f"{url}?v=6&encoding=json", proxy=self.proxy
            ) as ws:

                async for msg in ws:
                    data = json.loads(msg.data)
                    if data["op"] == 10:  # hello
                        asyncio.ensure_future(
                            self._heartbeat(ws, data["d"]["heartbeat_interval"])
                        )
                        await ws.send_json(
                            {
                                "op": 2,  # identify
                                "d": {
                                    "token": self.token,
                                    "properties": {},
                                    "compress": False,
                                    "large_threshold": 250,
                                },
                            }
                        )

                    elif data["op"] == 0:  # dispatch event
                        await self.handle_event(data)
