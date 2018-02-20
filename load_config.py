import configparser

settings = configparser.ConfigParser()
settings.read("settings/preferences.ini")

command_prefix = settings["Roxbot"]["Command_Prefix"]
token = settings["Roxbot"]["Token"]
owner = int(settings["Roxbot"]["OwnerID"])
tat_token = settings["Roxbot"]["Tatsumaki_Token"]


__description__ = """RoxBot, A Discord Bot made by a filthy Mercy Main. Built with love (and discord.py) by Roxxers#7443.

[Github link](https://github.com/RainbowDinoaur/roxbot)
[Changelog](https://github.com/RainbowDinoaur/roxbot#v100)"""
__author__ = "Roxanne Gibson"
__version__= "1.3.2"
embedcolour = 0xDEADBF


# IF YOU ARE TESTING OR NOT IN THE GSS DISCORD, REMOVE "cogs.gss" FROM THE LIST

cogs = [
	"cogs.admin",
	"cogs.fun",
	"cogs.customcommands",
	"cogs.joinleave",
	"cogs.nsfw",
	"cogs.reddit",
	"cogs.selfassign",
	"cogs.twitch",
	"cogs.util",
	"cogs.gss"
]
