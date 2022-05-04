"""
This module implements functionality for ingesting and managing the lineage
of bags.

Some main functions in this module will be called by the CLI.  Other helper
functions will be called only from within this module.

So far, this module is basically a stub.  It need to be implemented.
"""

# Import modules from the Python standard library
import sqlite3 as sq         # for SQLite DB interaction
import datetime as dt        # for getting and formatting timestamps
import time                  # for the sleep() function

# Import other SANCdpd modules
import conf
import logger as lg


###############################################################################
# function: show_agents
###############################################################################
def new_ingest():
    """
    This function ... well, it needs some work.
    """
    print("   Setting up new ingest operation...")
    time.sleep(2)
    print("   Standby...")
    time.sleep(3)
    print("   Preparing for ingest...\n")
    time.sleep(3)
    print("   Just kidding.  lol\n")
    time.sleep(5)
