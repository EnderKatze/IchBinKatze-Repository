import discord
from discord import Option
from discord.ext import commands
import json
import os
import Money

os.chdir("Json")

money = Money.Money()
bot = commands.Bot()
token = json.load(open("Config.json"))["token"]
currency = json.load(open("Config.json"))["currency"]


@bot.event
async def on_ready():
    print(f"Bot ready! ({bot.user.name})")


@bot.slash_command(name="getmoney", description="Get current money value of someone!", guild_ids=[798881392435134464])
async def userinfo(ctx, user: Option(discord.Member, "Money of which person?", required=False, default=None)):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.name}'s Accout:", color=discord.Colour.blue())
    embed.add_field(name="__Money:__", value=f"{money.getMoney(user.id)} **{currency}**")
    embed.set_footer(text="IchBinKatze v3 Bot")
    embed.set_thumbnail(url=user.avatar.url)
    await ctx.respond(embed=embed)


@bot.slash_command(name="addmoney", description="Set the money value of someone!", guild_ids=[798881392435134464])
async def addmoney(ctx, moneytoadd, user: Option(discord.Member, "Money of which person?",
                                                 required=False, default=None)):
    if user is None:
        user = ctx.author
    if ctx.author.guild_permissions.administrator:
        money.modifyMoney(user.id, moneytoadd)
        embed = discord.Embed(title="Success!", colour=discord.Colour.blue())
        embed.add_field(name=f"__{user.name} updated__",
                        value=f"{user.name} now has {money.getMoney(user.id)} **{currency}**")
        await ctx.respond(embed=embed)
    else:
        await ctx.respond(f"Sorry, {user.mention}, you don't have permissions to do this!")


bot.run(token)
