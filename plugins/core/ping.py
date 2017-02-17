# ping.py
# Tests Fox connectivity.

import sys
from plugins.plugin import FoxPlug
from util import Util
FoxPlug = FoxPlug()
util = Util()


if __name__ == "__main__":
    print(util.current_file() + " is a Fox plugin. It cannot be executed directly.")
    sys.exit()


def ping():
    return "Pong!"

