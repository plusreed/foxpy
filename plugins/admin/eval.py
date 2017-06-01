from discord.ext import commands
from plugins.utils import checks
import discord
import inspect
import datetime
from collections import Counter


class Eval:
    """Evaluator command for admins."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    # @checks.is_admin()
    async def eval(self, ctx, *, code: str):
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
            err_em = discord.Embed(
                title="Hit a snag!",
                description="I tried doing that but encountered an error.\n```py" + type(e).__name__ + ": " + str(e) + \
                            "```",
                colour=0x910000
            )

            err_em.set_author(
                name="Fox",
                icon_url=self.bot.user.avatar_url
            )

            await self.bot.say(embed=err_em)
            return

        result_em = discord.Embed(
            title="Results",
            description="Here's the results!\n" + py.format(result),
            colour=0x00AF19
        )

        result_em.set_author(
            name="Fox",
            icon_url=self.bot.user.avatar_url
        )

        await self.bot.say(embed=result_em)


def setup(bot):
    bot.add_cog(Eval(bot))
