"""
This module manages config information used by the rest of the SANCdpd package.

This module exposes several global variables for use by this and other modules:
    fconf: a dictionary of config values from the config file
    sconf: a dictionary of config values set a runtime (if any)
    event_types:  a list of event types from the database
    event_type_outcomes: a dictionary of lists of outcomes for each event type

The fconf variable is set by a function in this module.  Other variables are
set by functions in other modules.

The event_types and event_type_outcomes variables are useful for, among other
purposes, creating menus or select lists to allow the user to choose the
appropraite event types and the valid outcomes for a given event type.

This module depends on a valid SANCdpd config file.

It is expected that the config file is JSON with at least the following keys:
    logging: whether to enable logging ("true" or "false")
    logdir: path to logfile directory (ends with "/")
    dbfile: path to the SANCdpd SQLite database file
    person_agent_code: SANCdpd's code for the default person agent
    access_path_root: The path to the access storage location (ends with "/")
(Note that these match the req_conf_keys list defined below.)

This module contains the following function:
    readfile() :  Read the configuration file and write global fconf variable
"""

# Import modules from the Python standard library
import json                  # for reading the config file
import os.path               # for checking for the config file

# Import other SANCdpd modules
import logger as lg


###############################################################################
# Global (for this module) data structures, for sharing across modules
###############################################################################

# A list of the keys that should be found in the config file.  Program should
# raise an error or exception if any of these is missing.
req_conf_keys = ["logging",
                 "logdir",
                 "dbfile",
                 "person_agent_code",
                 "access_path_root"
                 ]

# Dictionary for config info from config file
# (This shouldn't change once readfile() has been run once.)
fconf = {}

# Dictionary for config info generated during currently running session
sconf = {}

# List of event types, queried from the database.
# Each event type is represented as an ordered triple as follows:
#    (event_type_code, event_name, event_category_code)
etypes = []

# Dictionary of lists of event outcomes, queried from the database.
# The key for each entry is an event_type_code
# The value for each entry is a list of outcomes typesfor that event_type
# Each outcome type is represented as an ordered pair as follows:
#    (outcome_code, outcome_name)
otypes = {}


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

    # check to make sure we have the required configuration keys
    for k in req_conf_keys:
        if k not in fconf.keys():
            raise Exception("Key '" + k + "' not found/read in config file.")
