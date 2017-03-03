# ping.py
# Test Fox's connectivity
from discord.ext import commands


class Ping:
    def __init__(self, bot):
        self.bot = bot

    async def ping(self):
        await self.bot.say("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
