# eval.py
# Evaluate Python code

from main import fox
import asyncio
from util import Util
from plugins.plugin import FoxPlug

util = Util()
FoxPlug = FoxPlug()


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