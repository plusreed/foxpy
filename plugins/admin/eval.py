# eval.py
# Evaluate Python code

from discord.ext import commands
from plugins.utils import checks
import discord
import inspect
import datetime
from collections import Counter


class FoxEval:
    async def evalpy(statement, message):
        try:
            evaled = eval(statement)
            em = fox.Embed(title='eval()', description="Here's what I got for that:\n" + evaled, colour=0x00AF19)
            em.set_author(name='Fox', icon_url=fox.user.default_user_url)
            await fox.send_message(message.channel, embed=em)
            return
        except:
            exc = Exception
            em = fox.Embed(title='eval()', description="I tried doing that but encountered an error.\n" + exc,
                           colour=0x910000)
            em.set_author(name='Fox', icon_url=fox.user.default_user_url)
            await fox.send_message(message.channel, embed=em)
            return

"""
@fox.event
async def on_message(a_message):
    if a_message.content.startswith(plg_cmd):
        statement = a_message.content
        try:
            final_eval = eval(statement)
            em = fox.Embed(title="eval()", description="Here's what I gof for that:\n" + final_eval, colour=0x00AF19)
            em.set_author(name="Fox", icon_url=fox.user.default_user_url)
            await fox.send_message(a_message.channel, embed=em)
            return
        except:
            exc = Exception
            em = fox.Embed(title='eval()', description="I tried doing that but encountered an error.\n" + exc,
                           colour=0x910000)
            em.set_author(name='Fox', icon_url=fox.user.default_user_url)
            await fox.send_message(a_message.channel, embed=em)
            return

plg_cmd = "$%eval"
"""


class Eval:
    """Evaluator command for admins."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    @checks.is_owner()
    async def eval(self, ctx, *, code : str):
        """Runs code through eval()."""
        code = code.strip('` ')
        py = '```py\n{}\n```'
        result = None

        env = {
            # sooner or later.
        }

        try:
            result = eval(code)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            # Make a fancy looking embed
            err_em = self.bot.Embed(
                title="Hit a snag!",
                description="I tried doing that but encountered an error.\n" + type(e).__name__ + ": " + str(e),
                colour=0x910000
            )

            err_em.set_author(
                name="Fox",
                icon_url=self.bot.user.default_user_url
            )

            await self.bot.say(embed=err_em)
            return

        result_em = self.bot.Embed(
            title="Results",
            description="Here's the results!\n" + py.format(result),
            colour=0x00AF19
        )

        result_em.set_author(
            name="Fox",
            icon_url=self.bot.user.default_user_url
        )

        await self.bot.say(embed=result_em)


def setup(bot):
    bot.add_cog(Eval(bot))
