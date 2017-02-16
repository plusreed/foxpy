# plugin.py
# The core to the plugin system


import plugins
import plugins.core


class fplg:
    @staticmethod
    def plugin_error(level, message):
        if level == 0:  # Info
            print("[fplg.INFO]: " + fplg.plugin_error.message)
        elif level == 1:  # Warning
            print("[fplg.WARN]: " + fplg.plugin_error.message)
        elif level == 2:  # Error
            print("[fplg.ERR]: " + fplg.plugin_error.message)
        elif level > 2:  # Level is bigger than 2
            print("[fplg.ERR]: fplg.plugin_error only uses error severity levels 0-2.")

