<h1 align="center">
  <br>
  <img src="/logo.svg?raw=true" alt="LightDiscord" width="256">
  <br>
</h1>


<h4 align="center">🤖 An ultra light library to develop discord bots with Python</h4>

# Get lightdiscord

To install the library without full voice support, you can just run the following command:
```console
# Linux/macOS
python3 -m pip install -U lightdiscord

# Windows
py -3 -m pip install -U lightdiscord
```

# Key features

* Easy to use and quick to learn
* Currently the smallest alternative to discord.py
* Support multiple bot instances
* Support custom listeners
* Full support for Bot and User accounts
* Low level: directly interact with the discord api and manage cache as you want

# How to use?

First, you need to ``import lightdiscord``. You can then create a bot object, specify a token and the events listener:
```python
bot = lightdiscord.Bot(
    "YOUR_TOKEN", listeners={"READY": on_ready}
)
```


You can check [https://github.com/Th0rgal/lightdiscord/blob/master/example.py](example.py)