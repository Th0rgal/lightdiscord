import lightdiscord
import asyncio


async def on_ready(bot_instance, data):
    user = data["d"]["user"]
    bot_instance.fullname = user["username"] + "#" + user["discriminator"]
    print(
        "> bot {user_display} loaded with id {bot_id}".format(
            user_display=bot_instance.fullname, bot_id=user["id"]
        )
    )


bot = lightdiscord.Bot("YOUR_TOKEN", listeners={"READY": on_ready})


async def main(loop):
    await bot.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
