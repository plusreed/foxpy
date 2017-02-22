from discord.ext import commands
import discord
import datetime, re
import asyncio
import copy
import logging
import traceback
import sys
from collections import Counter

description = """
I'm Fox, a multi-purpose and modular Discord bot.
"""


init_cogs = [
    'plugins.admin.eval',
    'plugins.admin.shutdown',
    'plugins.core.add',
    'plugins.core.ping',
]

dc_log = logging.getLogger(discord)
dc_log.setLevel(logging.DEBUG)
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='fox.log', encoding='utf-8', mode='w')
log.addHandler(handler)

hattr = dict(hidden=True)

prefix = ['$', '^']
fox = commands.Bot(command_prefix=prefix, description=description, pm_help=None, help_attrs=hattr)

@fox.event
async def on_command_error(error, ctx)
    if isinstance(error, commands.NoPrivateMessage):
        await fox.send_message(ctx.message.author, "Sorry, you can't use this command in private messages. :/")
    elif isinstance(error, commands.DisabledCommand):
        await fox.send_message(ctx.message.author, 'Sorry, it looks like that command is disabled.')
    elif isinstance(error, commands.CommandInvokeError):
        print('In {0.command.qualified_name}:'.format(ctx), file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print('{0.__class__.__name__}: {0}'.format(error.original), file=sys.stderr)

@fox.event
async def on_ready():
    print('Fox is now ready!')
    print('Username: ' + fox.user.name)
    print('ID: ' + fox.user.id)
    print('------')
    if not hasattr(fox, 'uptime'):
        fox.uptime = datetime.datetime.utcnow()

@fox.event
async def on_resumed():
    print("Fox has resumed.")

@fox.event
async def on_command(command, ctx):
    fox.commands_used[command.name] += 1
    message = ctx.message
    destination = None
    if message.channel.is_private:
        destination = 'Private Message'
    else:
        destination = '#{0.channel.name} ({0.server.name})'.format(message)

    log.info('{0.timestamp}: {0.author.name} in {1}: {0.content}'.format(message, destination))

@fox.event
async def on_message(message):
    if message.author.bot:
        return

    await fox.process_commands(message)
