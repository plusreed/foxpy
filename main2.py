import discord
from discord.ext import commands
import random
import config

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
fox = commands.Bot(command_prefix='$', description=description)


@fox.event
async def on_ready():
    print('Fox is ready.')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@fox.command()
async def pyeval(self, statement : str):
        try:
            final_eval = eval(statement)
            em = fox.Embed(title="eval()", description="Here's what I gof for that:\n" + final_eval, colour=0x00AF19)
            em.set_author(name="Fox", icon_url=fox.user.default_user_url)
            await self.fox.say(embed=em)
            return
        except:
            exc = Exception
            em = fox.Embed(title='eval()', description="I tried doing that but encountered an error.\n" + exc,
                           colour=0x910000)
            em.set_author(name='Fox', icon_url=fox.user.default_user_url)
            await self.fox.say(embed=em)
            return

fox.run(config.BOT_TOKEN)