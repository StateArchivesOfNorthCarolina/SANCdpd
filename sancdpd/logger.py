"""
This module creates and manages the runtime log files for SANCdpd.
It contains only two methods:
    begin() :  Tell logger to begin logging this session.
    log(msg) : Tell logger to add msg to session log.
"""

# Import modules from the Python standard library
import datetime as dt        # for getting and formatting timestamps
import os.path               # to make sure the log directory exists
import pprint                # for formatting the fconf dictionary for printing

# Import other SANCdpd modules
import conf


###############################################################################
# Global variable for the logfile filename.
###############################################################################
logfilename = ""


###############################################################################
# function: begin
###############################################################################
def begin():
    """
    Create a new timestamped log file for this session.
    (This should be run only once per SANCdpd session.)
    Begin logging by writing the first lines to it.
    """

    # If the conf file has not been read, for some reason, read it now.
    # Ordinarily this will not be necessary, unless this module is being run
    # directly.
    if conf.fconf == {}:
        print("Warning: Reading config file from logger module.")
        conf.readfile()
        print("fconf:", conf.fconf)

    # Make sure the directory for logfiles exists.
    if not os.path.exists(conf.fconf["logdir"]):
        raise Exception("Directory for log files does not exist.")

    # Create string with current timestamp.
    now = dt.datetime.now()
    strnow = now.strftime("%Y-%m-%d_%H-%M-%S_%f")

    # Construct a full filename.
    filename = conf.fconf["logdir"] + "sdpd_" + strnow + ".log"

    # Create, initialize, write actual logfile.
    fp = open(filename, "w")
    fp.write("SANCdpd logger activated at " +
             now.strftime("%Y-%m-%d %H:%M:%S.%f") +
             "\n")
    fp.write("SANCdpd is using the following values from the config file:" +
             "\n")
    fp.write(pprint.pformat(conf.fconf) + "\n")
    fp.close()

    # If we got here without a problem, set the global logfile filename
    global logfilename
    logfilename = filename

    # Output message to console informing user about logging.
    print("")
    print("   " + "Runtime logging activated.")
    print("   " + logfilename)
    print("")

    # Log first message.
    log("Logging begun successfully.")


###############################################################################
# function: log
###############################################################################
def log( message ):
    """
    Add a new line to the end of the logfile for this session.
    The line will include timestamp and the message.
    Note that the file gets opened, written, and closed for every log event.
    """

    # If logging is not enabled, simply exit with 1 status
    if not conf.fconf["logging"]:
        return 1

    # If we don't have a filename for logging, then error out
    if logfilename == "":
        raise Exception("Tried to log without a log file.")

    # create string with current timestamp
    now = dt.datetime.now()
    timestamp = "[" + now.strftime("%Y-%m-%d %H:%M:%S.%f") + "]"

    # append new line to the logfile and close logfile.
    fp = open(logfilename, "a")
    fp.write(timestamp + " " + message + "\n")
    fp.close()

    return 0
