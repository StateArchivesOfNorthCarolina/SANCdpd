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
# Global variable for the database connection
###############################################################################

#dbcon = ""  # is the needed?  Better to pass a connection around, when necessary?


###############################################################################
# function: test_connect
###############################################################################
def test_connect():
    """
    Tests whether there seems to be a valid SANCdpd database in the file
    specified by the config file.
    Fails with errors or exceptions if the file isn't found or if the database
    doesn't have basic event type reference tables.
    """

    # Check to see if the SANCdpd SQLite database exists
    if not os.path.exists(conf.fconf["dbfile"]):
        print("No file found at location:", conf.fconf["dbfile"])
        raise Exception("Database file not found.")

    # Create db connection
    con = sq.connect(conf.fconf["dbfile"])
    lg.log("test_connect: Connected to SQLite database at:" +
           conf.fconf["dbfile"])

    # Create cursor
    cur = con.cursor()

    # Query the event_type and event_type_outcome tables for diagnostics
    etypes = cur.execute("SELECT * FROM event_type").fetchall()
    otypes = cur.execute("SELECT * FROM event_type_outcome").fetchall()

    # If not much data in those tables, print warning (but no exception)
    if len(etypes) < 3 or len(otypes) < 2:
        print("Warning:  Little or no data in event reference tables.")

    cur.close()
    con.close()
    lg.log("test_connect: Database connection closed.")
