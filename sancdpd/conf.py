"""
This module manages config information used by the rest of the SANCdpd package.

It creates and sets global data structures, for sharing across modules.

It depends on the existence of a SANCdpd config file and a SANCdpd database.

It is expected that the config file is JSON with at least the following keys:
    logging: whether to enable logging ("true" or "false")
    logdir: path to logfile directory (ends with "/")
    dbfile: path to the SANCdpd SQLite database file
    person_agent_code: SANCdpd's code for the default person agent
"""

# Import modules from the Python standard library
import json                  # for reading the config file
import os.path               # for checking for the config file


###############################################################################
# Global (for this module) data structures, for sharing across modules
###############################################################################

# Dictionary for config info from config file
# (This shouldn't change once readfile() has been run once.)
fconf = {}

# Dictionary for confg info set within the current session
sconf = {}


###############################################################################
# function: readfile
###############################################################################
def readfile():
    """
    Read a config file to initialize global variables.
    If a required config value is missing or invalid, raise an exception.
    """

    # The name of the config file to look for
    configfilename = "SANCdpd_config.json"

    # The list of locations where we will look for the config file
    trylocs = [
        "./",
        "../",
        "./SANCdpd/",
        "../SANCdpd/"
        ]

    # Search for the config file in the list of locations.  Stop when found
    found = False
    for loc in trylocs:
        pathtofile = loc + configfilename
        if os.path.exists(pathtofile):
            found = True
            break

    # Raise and exception and error out if we don't have a config file.
    if not found:
        raise Exception("SANCdpd config file not found.")

    # create a global variable to store config information
    global fconf
    fconf = {}

    # load the global conf dictionary from the JSON file
    conffp = open(pathtofile, "r")
    fconf = json.load(conffp)
    conffp.close()



###############################################################################
# function: validate
###############################################################################
def validate():
    """Validate the configuration and the database connection."""

    # check the database connection
    # check whether the database appears valid
