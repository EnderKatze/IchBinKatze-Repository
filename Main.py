import discord
from discord import Option
from discord.ext import commands
import json
import os
import utils

#os.chdir("./Json")

# You will need a Config.json (Example file in /Json) and some other json files
# - Experience.json

level = utils.Level()
bot = commands.Bot()
token = json.load(open("./Json/Config.json"))["token"]
cogfiles = [f"cogs.{filename[:-3]}" for filename in os.listdir("cogs/") if filename.endswith(".py")]
for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as exception:
        print(exception)


@bot.event
async def on_ready():
    print(f"Bot ready! ({bot.user.name})")


bot.run(token)
