"""
This module manages config information used by the rest of the SANCdpd package.

It creates and sets global data structures, for sharing across modules.

It depends on the existence of a SANCdpd config file and a SANCdpd database.

It is expected that the config file is JSON with at least the following keys:
    logging: whether to enable logging ("true" or "false")
    logdir: path to logfile directory (ends with "/")
    dbfile: path to the SANCdpd SQLite database file
    person_agent_code: SANCdpd's code for the default person agent

This module exposes several global variables for use by this and other modules:
    fconf: a dictionary of config values from the config file
    event_types:  a list of event types from the database
    event_type_outcomes: a dictionary of lists of outcomes for each event type

This module contains two functions:
    readfile() :  Read the configuration file and write global fconf variable
    loadref() : Read database reference tables and write global lists
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

# List of event types, queried from the database.
# Each event type is represented as an ordered triple as follows:
#    (event_type_code, event_name, event_category_code)
event_types = []

# Dictionary of lists of event outcomes, queried from the database.
# The key for each entry is an event_type_code
# The value for each entry is a list of outcome_code's for that event_type
event_type_outcomes = {}


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

    # Raise an exception and error out if we don't have a config file.
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
# function: loadref
###############################################################################
def loadref():
    """
    Load data from database reference tables for easy access.
    Create global variables with data structures capturing records from
        `event_type`
        `event_type_outcome`
    """
    # need to implement
    pass
