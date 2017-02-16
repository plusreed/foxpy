# This is an example plugin.
# It's recommended you base your plugin off of this.
# This also shows basic usage of FoxPlug, the class for making Fox plugins.

from plugins.plugin import FoxPlug
from util import Util
FoxPlug = FoxPlug()
util = Util()

# I highly recommend putting this code at the top of plugins (after imports, of course)
if __name__ == "__main__":
    print(util.current_file() + " is a Fox plugin and cannot be directly executed.")

FoxPlug.plugin_error(0, "example.py started!")
print("Hello, world!")
