# add.py
# Fox plugin for adding numbers together

from discord.ext import commands


class FoxMath:
    """Wait... Foxes know how to do math...?"""

    def __init__(self, bot):
        self.bot = bot

    def add(self, *, num: float):
        num = None

    def subtract(self, *, num: float):
        num = None

    def multiply(self, *, num: float):
        num = None

    def divide(self, *, num: float):
        num = None


def setup(bot):
    bot.add_cog(FoxMath(bot))
