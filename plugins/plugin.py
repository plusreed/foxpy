# plugin.py
# The core to the plugin system


import sys
from main import fox
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
            del message
            # print("[fplg.ERR]: " + util.current_file() + " is a Fox plugin. It cannot be executed directly.")
            return "WARNING: Plugin error level 3 is deprecated and shouldn't be used. Use FoxPlug.check_scriptexec()."
        elif level > 3:  # Level is bigger than 2
            print("[fplg.ERR]: fplg.plugin_error only uses error severity levels 0-3.")

    def check_scriptexec(message):
        if __name__ == "__main__":
            if message is None:
                print(util.current_file() + " is a Fox plugin. It cannot be executed directly.")
            else:
                print("[" + util.current_file() + "]: " + message)
        else:
            return

    def register_plugin(plg_name, plg_version, plg_author, plg_cmd, func):
        @fox.event
        async def on_message(message):
            if message.content.startswith(plg_cmd):
                name = plg_name
                ver = plg_version
                author = plg_author
                func
