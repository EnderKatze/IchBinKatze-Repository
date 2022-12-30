import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import Main


class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.level = Main.level

    @slash_command(name="stats", description="Get somebody's stats!",
                   guild_ids=[798881392435134464])
    async def level(self, ctx, user: Option(discord.Member, "Stats of which person? (Optional)", required=False, default=None)):

        if user == None:
            user = ctx.author

        if ctx.author.name.endswith("s"):
            title = f"{ctx.author.name}' Level"
        else:
            title = f"{ctx.author.name}'s Level"

        embed = discord.Embed(title=title, colour=discord.Colour.blue())

        levelList = self.level.getLevel(user.id)
        expToNextLevel = ((levelList[0]) * 100 * 1.25) - levelList[1]

        embed.add_field(name="__Level__", value="**" + str(levelList[0]) + "**" + f" ({expToNextLevel} Exp to next Level)")

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(StatsCog(bot))