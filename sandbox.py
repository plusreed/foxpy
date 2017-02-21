# sandbox.py
# Fox's plugin sandbox

import os
import sys
import plugins
import plugins.plugin
import plugins.core
import mmap


class PlgSandbox:
    NASandbox = {
        # This is an array of SHA256 hashes in which the sandbox will not apply to.
        "64d8cb16e676730cd1f280b9eacad4d8b5c2cc8076a0c42b8d7fecd5564e1eb2"  # core/add.py
    }

    def check_sysexit(self):
        with open(self, 'rb', 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as check:
            if check.find(b'sys.exit') != -1:
                print("[fplg.sandbox] Plugin " + self + " attempted to use sys.exit and was blocked")

