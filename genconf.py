# genconf.py
# Generate a fox_config.json


import os
import sys
import json
import click


@click.command()
@click.option("--new-conf", prompt="New configuration name", help="Generate a new configuration file")

def sanity(stage):
    # Sanity checks
    # We need to check the working directory for 'fox_config.json'
    if os.path.isfile("..\fox_config.json"):
        print("fox_config.json already exists.")
        del stage  # As a sanity check failed, stage will be removed.
        sys.exit()  # Exit genconf.
    else:
        # Passed stage 1 sanity check
        # Currently this is the only sanity stage, there should be more probably
        print("Sanity checks passed.")


def welcome():
    """Welcome function for CLI"""
    print("genconf.py")
    print("ver 0.1, beta")
    print("Please report bugs to https://github.com/plusreed/foxpy")
    sanity()

welcome()
