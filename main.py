# Fox, rewritten in Python for literally no reason at all.


import logging
import os
import discord
import config
import plugins.admin

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='fox.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

print("Just a moment, Fox is initializing...")
fox = discord.Client()

print("[fplg] Scanning for plugins... this might take a minute or two.")
plg_dir = "\plugins"

for root, subdirs, files in os.walk(plg_dir):
    print("[fplg.scanner] Found " + root)


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
        from plugins import ping
        await fox.send_message(message.channel, ping.ping())

    # TODO: find some better way to do this because this can get ugly real fast
    if message.content.startswith("$myavatar") or message.content.startswith("$myavi"):
            from plugins import avatar  # Not a plugin yet
            avatar.get_avatar(message.author.default_avatar_url)

    if message.content.startswith("$shutdown"):
            from.plugins.admin.shutdown import shutdown
            await fox.send_message(message.channel, "Shutting down.")
            # shutdown.shutdown()
            import sys
            sys.exit()

    if message.content.startswith("$%eval"):
        from plugins.admin.eval import FoxEval
        FoxEval.evalpy(message.content)


@fox.event
async def on_message(a_message):
    # We need to check the ID of the user who sent the message
    if a_message.author.id in config.ADMINS:
        if a_message.content.startswith("$%shutdown"):
            from plugins.admin import shutdown
            shutdown.shutdown()
            return

        if a_message.content.startswith("$%admin"):
            await fox.send_message(a_message.channel, "You seem to be in the admin table. Therefore, you are an admin!")
            return

    else:
        admin_cmds = [
            "$%shutdown",
            "$%admin"
        ]
        if a_message.content.startswith("$%") and a_message.content in admin_cmds:
            await fox.send_message(a_message.channel, "You don't have permission to use this command.")
            if config.DEBUG:
                str1 = ', '.join(str(e) for e in config.ADMINS)
                await fox.send_message(a_message.channel, "**[debug]**: current admin ids: `" + str1 + "`")
                await fox.send_message(a_message.channel, "**[debug]**: message content: " + a_message.content)
                return
            else:
                return
        else:
            return


fox.run(config.BOT_TOKEN)
