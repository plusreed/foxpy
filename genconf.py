# genconf.py
# Generate a fox_config.json

import json
import click

@click.command()
@click.option('--new-conf', prompt='New configuration name', help='Generate a new configuration file')

def welcome():
    """Function that welcomes the user"""
    print("genconf.py")
    print("ver 0.1, beta")
    print("Please report bugs to https://github.com/plusreed/foxpy\n")
