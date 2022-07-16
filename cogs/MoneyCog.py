from Main import currency
from classes import Money
import discord
from discord.ext import commands
from discord.commands import slash_command, Option

money = Money()


class MoneyCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name="userinfo", description="Get current money value of someone!",
                   guild_ids=[798881392435134464])
    async def userinfo(self, ctx, user: Option(discord.Member, "Money of which person?", required=False, default=None)):
        if user is None:
            user = ctx.author
        embed = discord.Embed(title=f"{user.name}'s Accout:", color=discord.Colour.blue())
        embed.add_field(name="__Money:__", value=f"{money.getMoney(user.id)} **{currency}**")
        embed.set_footer(text="IchBinKatze v3 Bot")
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.respond(embed=embed)

    @slash_command(name="modifymoney", description="Set the money value of someone!",
                   guild_ids=[798881392435134464])
    async def modifymoney(self, ctx, modifyvalue,
                          user: Option(discord.Member, "Money of which person?", required=False, default=None)):
        if user is None:
            user = ctx.author
        if ctx.author.id == 698113221051154453:
            money.modifyMoney(user.id, modifyvalue)
            embed = discord.Embed(title="Success!", colour=discord.Colour.blue())
            embed.add_field(name=f"__{user.name} updated__",
                            value=f"{user.name} now has {money.getMoney(user.id)} **{currency}**")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond(f"Sorry, {user.mention}, you don't have permissions to do this!")


def setup(bot):
    bot.add_cog(MoneyCog(bot))
