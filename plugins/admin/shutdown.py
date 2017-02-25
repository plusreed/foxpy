from discord.ext import commands
from plugins.utils import checks
import discord
import sys


class Shutdown:
    """Shutdown the Discord bot."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    @checks.is_owner()
    async def shutdown(self, ctx, *, shutdown_id: int):
        # We need to log out of Fox first.
        await self.bot.logout()
        if shutdown_id is None:
            print("Logged out of Fox. See ya! (Shutdown ID: 0)")
            sys.exit(0)
        else:
            print("Logged out of Fox. See ya! (Shutdown ID: " + str(shutdown_id) + ")")
            sys.exit(shutdown_id)


def setup(bot):
    bot.add_cog(Shutdown(bot))
