# lastfm.py
# Last.fm plugin for Fox

from discord.ext import commands
import config


class LastFm:
    user = None
    api_key = config.LFM_API_KEY
    base_url = "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={0}&api_key={1}&format=json".format(user,
                                                                                                               api_key)

    def __init__(self, bot):
        self.bot = bot

