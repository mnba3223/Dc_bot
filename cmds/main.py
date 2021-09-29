import discord
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension



class Main(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} (ms)')

def setup(bot):
    bot.add_cog(Main(bot))