# shutdown.py
# Shuts the bot down.

import sys
from util import Util
from plugins.plugin import FoxPlug

util = Util()
FoxPlug = FoxPlug()


if __name__ == "__main__":
    print(util.current_file() + " is a Fox plugin. It cannot be executed directly.")
    sys.exit()


class shutdown:
    """Admin class: shutdown"""
    def shutdown(self):
        """Forcibly shuts down Discord bot"""
        sys.exit(self)

