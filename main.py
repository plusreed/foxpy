# Fox, rewritten in Python for literally no reason at all.


import discord
import asyncio
import plugins
import config
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='fox.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print("Just a moment, Fox is initializing...")
fox = discord.Client()


@fox.event
async def on_ready():
    print('------')
    print('Fox is ready!')
    print('Fox username: ' + fox.user.name)
    print('Fox user ID: ' + fox.user.id)
    print('------')


@fox.event
async def on_message(message):
    if message.content.startswith("$ping"):
        from plugins.core import ping
        await fox.send_message(message.channel, ping.ping())


fox.run(config.BOT_TOKEN)
