<h1 align="center">
  <br>
  <img src="/logo.svg?raw=true" alt="LightDiscord" width="256">
  <br>
</h1>


<h4 align="center">🤖 An ultra light library to develop discord bots with Python</h4>

# Get lightdiscord

To install the library, you can just run the following command:
```console
# Linux/macOS
python3 -m pip install -U lightdiscord

# Windows
py -3 -m pip install -U lightdiscord
```

# Key features

> :warning: If the size of the library and the proximity with the discord api is not absolutely necessary for you, [https://github.com/Rapptz/discord.py](discord.py) may be a better option.

* Easy to use and quick to learn
* Currently the smallest alternative to discord.py
* Support custom listeners
* Support multiple bot instances
* Full support for Bot and User accounts
* Support proxies
* Customizable user agent
* Low level: directly interact with the discord api and manage cache as you want


# How to use?

First, you need to ``import lightdiscord``. You can then create a bot object, specify a token and optional features:

- *user*: A boolean (True for user accounts, False by default)
- *listeners*: A dictionnary containing your events listeners and the API endpoint
- *proxy*: A proxy (None for no proxies, None by default)
- *user_agent*: The user agent sent to discord


```python
bot = lightdiscord.Bot(
    "YOUR_TOKEN", listeners={"READY": on_ready}
)
```

To start the bot, you need to use an async function. Here is an example with asyncio
```python
import asyncio

async def main(loop):
    await bot.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
```

You can check [https://github.com/Th0rgal/lightdiscord/blob/master/example.py](example.py)