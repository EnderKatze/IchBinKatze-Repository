import discord
from discord import Option
from discord.ext import commands
import json
import os
import classes

os.chdir("./Json")

money = classes.Money()
bot = commands.Bot()
token = json.load(open("Config.json"))["token"]
currency = json.load(open("Config.json"))["currency"]

os.chdir("..")

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as exception:
        print(exception)


os.chdir("./Json")


@bot.event
async def on_ready():
    print(f"Bot ready! ({bot.user.name})")


bot.run(token)
