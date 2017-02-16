# add.py
# Fox plugin for adding numbers together

import sys
from plugins.plugin import FoxPlug
from util import Util
FoxPlug = FoxPlug()
util = Util()

if __name__ == "__main__":
    print(util.current_file() + " is a Fox plugin. It cannot be executed directly.")
    sys.exit()


def add(num1, num2):
    number1 = float(num1)
    number2 = float(num2)
    val = number1 + number2
    return val
