# util.py
# Used for making some functions easier to handle.

import os
import sys


class Util:
    @staticmethod
    def current_file():
        """Returns the currently running script file name."""
        return os.path.basename(sys.argv[0])
