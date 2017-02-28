# voice.py
# Voice handler for Discord

import discord
import asyncio
from discord.ext import commands
from plugins.utils import checks


class VoiceHandler:

    def __init__(self, bot):
        self.bot = bot

    async def joinchannel(self, id: int, name: str, message):
        if message.author.voice.voice_channel is None:
            await self.bot.say("Sorry, I couldn't do that. You're not in a voice channel.")
            await self.bot.say("I can join a voice channel in this server if you append the `joinchannel` command with"
                               "a voice channel ID.")
        else:
            try:
                self.bot.join_voice_channel(message.author.voice.voice_channel)
            except discord.InvalidArgument:
                # await self.bot.say("Sorry, looks like that ID isn't a voice channel ID.")
                return
            except asyncio.TimeoutError:
                await self.bot.say("Couldn't connect to the voice channel in time.")
                return
            except discord.ClientException:
                await self.bot.say("Sorry, it looks like I'm already connected to a voice channel.")
                return
            except discord.opus.OpusNotLoaded:
                await self.bot.say("Whoops, `libopus` isn't loaded.")
                return
            finally:
                await self.bot.say("Joined the voice channel! Hello, **" + discord.VoiceClient.channel.name + "**!")

        """
        # This is commented out because I don't know if it'll work.
        elif id:
            await self.bot.say("Please wait, I'm trying to find that channel...")
            try:
                self.bot.join_voice_channel(id)
            except discord.InvalidArgument:
                await self.bot.say("Sorry, looks like that ID isn't a voice channel ID.")
            except asyncio.TimeoutError:
                await self.bot.say("Couldn't connect to the voice channel in time.")
            except discord.ClientException:
                await self.bot.say("Sorry, it looks like I'm already connected to a voice channel.")
            except discord.opus.OpusNotLoaded:
                await self.bot.say("Whoops, `libopus` isn't loaded.")
            finally:
                await self.bot.say("Successfully resolved the ID.")
                await self.bot.say("Joined the voice channel! Hello, **" + discord.VoiceClient.channel.name + "**!")
                # Load opus in the background
                discord.opus.load_opus()
            """

