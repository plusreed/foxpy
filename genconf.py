# genconf.py
# Generate a fox_config.json

import os
import sys
import json
import click

@click.command()
@click.option('--new-conf', prompt='New configuration name', help='Generate a new configuration file')

def welcome():
    """Function that welcomes the user"""
    print("genconf.py")
    print("ver 0.1, beta")
    print("Please report bugs to https://github.com/plusreed/foxpy\n")
    sanity()

def sanity(stage):
    # Sanity checks
    # We need to check the working directory for 'fox_config.json'
    stage = 1
    if os.path.isfile("..\fox_config.json"):
        print("fox_config.json already exists.")
        stage = 0
        sys.exit()
    else:
        # Passed stage 1 sanity check
        # Currently this is the only sanity stage, there should be more probably
