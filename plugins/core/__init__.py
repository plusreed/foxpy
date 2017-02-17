# Not used at the moment.
# This code basically gets all the plugins from the folder.
"""
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f)]
"""