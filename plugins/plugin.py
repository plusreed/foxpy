# plugin.py
# The core to the plugin system


import plugins
import plugins.core
import sys
from util import Util
util = Util()


if __name__ == "__main__":
    print(util.current_file() + " is the core plugin system for Fox. It cannot be executed directly.")
    sys.exit()


class FoxPlug:
    @staticmethod
    def plugin_error(level, message):
        if level == 0:  # Info
            print("[fplg.INFO]: " + message)
        elif level == 1:  # Warning
            print("[fplg.WARN]: " + message)
        elif level == 2:  # Error
            print("[fplg.ERR]: " + message)
        elif level == 3:  # Plugin being executed directly
            # message = None
            print("[fplg.ERR]: " + util.current_file() + " is a Fox plugin. It cannot be executed directly.")
        elif level > 3:  # Level is bigger than 2
            print("[fplg.ERR]: fplg.plugin_error only uses error severity levels 0-3.")
