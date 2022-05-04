"""
This module manages interaction with the SANCdpd database.

The SANCdpd database is structured according to the schema specified and
described in the SANCdpd data dictionary.  The database itself is created in
SQLite version 3.

This module contains the following functions:
    checkdb(): Checks connection and does basic validation of the database
    loadref() : Read database reference tables and write global lists
"""

# Import modules from the Python standard library
import os.path               # to make sure the database file exists
import sqlite3 as sq         # for SQLite DB interaction
import datetime as dt        # for getting and formatting timestamps


# Import other SANCdpd modules
import conf
import logger as lg


###############################################################################
# function: check_db
###############################################################################
def check_db():
    """
    Tests whether there seems to be a valid SANCdpd database in the file
    specified by the config file.
    Fails with errors or exceptions if any of the following:
      - the file isn't found
      - the database doesn't have basic event type reference tables
      - the person agent from config file is not in the agents table
    """

    # Check to see if the SANCdpd SQLite database exists
    if not os.path.exists(conf.fconf["dbfile"]):
        print("No file found at location:", conf.fconf["dbfile"])
        raise Exception("Database file not found.")

    # Create db connection and cursor
    con = sq.connect(conf.fconf["dbfile"])
    lg.log("check_db: Successfully connected to SQLite database at:" +
           conf.fconf["dbfile"])
    cur = con.cursor()

    # Now, do some basic queries to see if it looks like a real SANCdpd db

    # Query the event_type and event_type_outcome tables for diagnostics
    evttypes = cur.execute("SELECT * FROM event_type").fetchall()
    outtypes = cur.execute("SELECT * FROM event_type_outcome").fetchall()

    # If not much data in those tables, print warning (but no exception)
    if len(evttypes) < 3 or len(outtypes) < 2:
        print("Warning:  Little or no data in event reference tables.")


    # Query the agents table to confirm the agent specified in the config file
    # is an active person agent in the database
    qstr = """SELECT agent_name, agent_code
              FROM agent
              WHERE agent_code = ?"""
    qargs = (conf.fconf["person_agent_code"],)
    agentrows = cur.execute(qstr, qargs).fetchall()

    if len(agentrows) != 1:
        erstr = "Person agent from config file not uniquely in agents table."
        raise Exception(erstr)

    lg.log("Active person agent " +
           agentrows[0][0] + " (" + agentrows[0][1] + ") " +
           "found in database.")

    # Close cursor and connection
    cur.close()
    con.close()


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

    # Create db connection and cursor
    con = sq.connect(conf.fconf["dbfile"])
    cur = con.cursor()


    # Query event_type and set global list
    qstr = """SELECT event_type_code, event_name, event_category_code
              FROM event_type"""
    conf.etypes = cur.execute(qstr).fetchall()

    lg.log("loadref: Loaded values from event_type table")


    # Create global dictionary of outcomes

    # First, writ the query string to get the otypes for a given etype
    qstr = """SELECT outcome_code, outcome_name
              FROM event_type_outcome
              WHERE event_type_code = ?"""

    # Loop through the etypes to set valid otypes for each
    for et in conf.etypes:
        qargs = (et[0],)
        conf.otypes[et[0]] = cur.execute(qstr, qargs).fetchall()

    lg.log("loadref: Loaded values from event_type_outcome table")


    # Close cursor and connection
    cur.close()
    con.close()
