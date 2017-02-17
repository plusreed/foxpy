# Fox, rewritten in Python for literally no reason at all.


import discord
import asyncio
import plugins
import config


print("Just a moment, Fox is initializing...")
fox = discord.Client()


@fox.event
async def on_ready():
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
