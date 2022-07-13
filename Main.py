import discord
from discord import Option
from discord.ext import commands
import json
import os
from Money import Money

os.chdir("Json")

moneyClass = Money()
bot = commands.Bot()
token = json.load(open("Config.json"))["token"]
currency = json.load(open("Config.json"))["currency"]

@bot.event
async def on_ready():
    print(f"Bot ready! ({bot.user.name})")


@bot.event
async def on_message(message):
    with open("Money.json", "r") as f:
        moneyList = json.load(f)
    if not str(message.author.id) in moneyList:
        moneyList[str(message.author.id)] = 0
    with open("Money.json", "w") as f:
        json.dump(moneyList, f)


@bot.slash_command(name="getmoney", description="Get current money value of someone!", guild_ids=[798881392435134464])
async def userinfo(ctx, user: Option(discord.Member, "Money of which person?", required=False, default=None)):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.name}'s Accout:", color=discord.Colour.blue())
    embed.add_field(name="__Money:__", value=f"{Money.getMoney()} **{currency}**")
    embed.set_footer(text="IchBinKatze v3 Bot")
    embed.set_thumbnail(url=user.avatar.url)
    await ctx.respond(embed=embed)


@bot.slash_command(name="addmoney", description="Set the money value of someone!", guild_ids=[798881392435134464])
async def addmoney(ctx, moneytoadd, user: Option(discord.Member, "Money of which person?",
                                                 required=False, default=None)):
    if user is None:
        user = ctx.author
    if ctx.author.guild_permissions.administrator:
        print(user.id)
        Money.addMoney(moneytoadd)
        await ctx.respond(f"Added {str(moneytoadd)} Katz-Coin to {user.name}'s Account")
    else:
        await ctx.respond(f"Sorry, {user.mention}, you don't have permissions to do this!")


bot.run(token)
