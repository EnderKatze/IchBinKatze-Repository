import discord
from discord.ext import commands
from discord.commands import slash_command
import Main


class GithubCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name="bugtracker", description="get a link to the github issues page",
                   guild_ids=[798881392435134464])
    async def bugtracker(self, ctx):
        embed = discord.Embed(title="Bugtracker", colour=discord.Colour.blue())
        embed.add_field(name="Please report issues here:", value="https://github.com/EnderKatze/IchBinKatze-Repository/issues/new")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(GithubCog(bot))
