"""
This module manages interaction with the SANCdpd database.

The SANCdpd database is structured according to the schema specified and
described in the SANCdpd data dictionary.  The database itself is created in
SQLite version 3.


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

    # Create db connection
    con = sq.connect(conf.fconf["dbfile"])
    lg.log("Successfully connected to SQLite database at:" +
           conf.fconf["dbfile"])

    # Do some basic queries to see if it looks like a real SANCdpd database

    # Create cursor
    cur = con.cursor()


    # Query the event_type and event_type_outcome tables for diagnostics
    etypes = cur.execute("SELECT * FROM event_type").fetchall()
    otypes = cur.execute("SELECT * FROM event_type_outcome").fetchall()

    # If not much data in those tables, print warning (but no exception)
    if len(etypes) < 3 or len(otypes) < 2:
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
    lg.log("Database connection closed.")
