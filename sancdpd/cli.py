"""
This module runs the CLI for SANCdpd.

This module includes these functions:
    startcli() :  Starts the CLI by running other functions
    welcome() :  Just prints a welcome message
    run_menu() :  Implements the CLI menu system
    run_proc() :  Passes control to the procedure to be run

This module also defines a global data structure called menudefs, which defines
the menus displayed by run_menu().

"""

# Import modules from the Python standard library
import time                  # for the sleep() function

# Import other SANCdpd modules
import conf
import logger as lg
import dbops

# Import SANCdpd modules for running operational scenarios
import operational.bagmgmt
import operational.agentmgmt


# The name of the software agent currently running, as known to the SANCdpd
# database in the `agent`.`agent_name` field.
SOFTW_AGENT_NAME = "SANCdpd CLI"

# Update the version number as appropriate
# Must match the `agent`.`agent_version` field in the SANCdpd database
VERSION = "0.1.0"


###############################################################################
# function: welcome
###############################################################################
def welcome():
    """
    Prints a welcome message
    """
    print("")
    print("**************************")
    print("*                        *")
    print("    " + SOFTW_AGENT_NAME)
    print("*                        *")
    print("    (ver " + VERSION + ")")
    print("*                        *")
    print("**************************")



###############################################################################
# dictionary: menudefs
###############################################################################
# This dictionary defines the menus for the SANCdpd CLI
# The dictionary key is the internal (non-display) menukey for the menu.
# Submenus are created by including the menukey as an option within a menu
# For each menukey, there is a list that defines one menu.
# The first list item is the title (breadcrumb name) of the menu.
# Each addditional list item is a 4-tuple.
# Each 4-tuple includes:
#    - the option's keyboard command (1-3 lowercase alphanumeric characters)
#    - the option's description (for menu display purposes only)
#    - the options's action type: "menu", "proc", "back", "quit"
#    - the menu or proc key
#      (which links to other menus or says which procedure to run)
# Notes on ordering:
#    - Within a menu, the order of the options matters.
#    - The order in which menus are defined in the menudefs dictionary does
#      not matter
# Note about the code formatting:
#    - The formatting of the following code defining the dictionary is not
#      very Pythonic.  This formatting has been used for the special purpose of
#      making it easy to read and edit the menus.
###############################################################################
menudefs = {\
"main": ["MAIN MENU",
    ("n", "Perform new ingest", "proc", "ingest"),
    ("e", "Record administrative events", "menu", "recevents"),
    ("l", "Evolve lineage", "menu", "lineage"),
    ("c", "Create or register access copies", "menu", "access"),
    ("r", "Generate reports", "menu", "reports"),
    ("a", "Manage agents", "menu", "agent"),
    ("s", "Manage storage", "menu", "storage"),
    ("q", "Quit SANCdpd CLI", "quit", "")
    ],
"recevents": ["Event Recording",
    ("b", "Go back", "back", "")
    ],
"lineage": ["Lineage Evolution",
    ("b", "Go back", "back", "")
    ],
"access": ["Access Copies",
    ("b", "Go back", "back", "")
    ],
"reports": ["Reports",
    ("b", "Go back", "back", "")
    ],
"agent": ["Agent Management",
    ("s", "Show active agents", "proc", "show_agents"),
    ("a", "Add new agent", "proc", "add_agent"),
    ("d", "Deactivate agent", "proc", "deactivate_agent"),
    ("b", "Go back", "back", "")
    ],
"storage": ["Storage Management",
    ("s", "Show active storage locations", "proc", "show_storage"),
    ("a", "Add new storage location", "proc", "add_storage"),
    ("d", "Deactivate storage", "proc", "deactivate_storage"),
    ("b", "Go back", "back", "")
    ]
}



###############################################################################
# function: run_menu
###############################################################################
def run_menu(branch):
    """
    This function handles display and interaction with the CLI menu.
    It takes as its input a non-empty list of menukeys.  The list, from left
    to right, captures the menu navigation depth, and is used for displaying
    navigation breadcrumbs.  The last item in the list is the menukey for
    the current menu to display.

    This function depends on the menudefs dictionary (which is defined globally
    for this module).  All menu content is defined in menudefs.
    This function assumes that menudefs has a particular structure.

    Note that this is a recursive function:  It can call itself, based on user
    input, to generate the next level of menu.  When the "quit" command is
    received, that is the base case of the recusion, in which it does not call
    itself again.  It will return control to the function that called it, which
    might be itself, or might the start_cli function.
    """

    # Create very slight pause to make console interaction feel more intuitive
    time.sleep(0.3)

    # Create and print string of navigation breadcrumbs based on the branch
    crumbs = ""
    for menu in branch:
        crumbs += (">> " + menudefs[menu][0] + "  ")
    crumbs += ">>"
    print("\n")
    print("".join([">" for i in range(len(crumbs))]))
    print(crumbs)
    print("".join([">" for i in range(len(crumbs))]))


    # Display the options for the last level in this branch.
    # We get the last menu in the branch, and iterate through through the
    # option tuples in that menu.
    for op in menudefs[branch[-1]][1:]:
        print("   " + op[0] + "\t" + op[1])


    # Variables to capture the menu action
    next_action = ""
    action_spec = ""

    # Loop input prompt until we get valid user input
    while next_action == "":
        # Get raw user input from prompt
        rawin = input("?> ")

        # Very short pause
        time.sleep(0.1)

        # Take only the first three characters, and make letters lowercase
        normin = rawin[:3].lower()

        # Check to see if input matches a valid option in the current menu
        for op in menudefs[branch[-1]][1:]:
            if normin == op[0]:
                next_action = op[2]
                action_spec = op[3]

        # If the we didn't manage to set the next action, the input was invalid
        if next_action == "":
            print("-- Invalid entry. --")


    # Take the appropriate action based on the type of next action

    if next_action == "menu":
        # Add a level to the branch and run the menu
        run_menu(branch + [action_spec])

    elif next_action == "back":
        # Run the menu without the last level of the branch
        run_menu(branch[:-1])

    elif next_action == "proc":
        # Run the procedure specified, by passing the option to run_proc
        run_proc(action_spec)

        # After running the procedure, run menu from the same level
        run_menu(branch)

    elif next_action == "quit":
        # Note that this option does not directly call an exit function.
        # It "quits" simply by not calling the run_menu function again.
        # Thus, it is the base case of the recursion.
        lg.log("run_menu: Received 'quit' command from menu.  Returning.")
        print("\n   Exiting the SANCdpd CLI menu system now.  Goodbye.\n")

    # If control is returned to the menu with no further directive, then exit
    # with normal status.
    return 0



###############################################################################
# function: run_proc
###############################################################################
def run_proc(procname):
    """
    This function take a procname, as specified in a menu option, and executes
    the relevant commands.

    This function basically serves as a switch statement that takes a menu
    command and then executes the relevant procedure.

    There should be one "if" or "elif" clause for each procname used in the
    menu system.

    Typically, there will be only a few lines of code for each of the possible
    menu comands, because control will quicly be handed off to a function in
    the module for the relevant operational scenario.
    """

    lg.log("Menu command: " + procname + ". Will attempt to execute.")

    if procname == "ingest":
        operational.bagmgmt.new_ingest()

    elif procname == "show_agents":
        operational.agentmgmt.show_agents()

    else:
        print("   Procedure '" + procname + "' not yet implemented.")

    input("   Press Enter to continue.")



###############################################################################
# function: start_cli
###############################################################################
def startcli():
    """
    This is the first function that should be run for the CLI.
    """

    # Print intial welcome message for SANCdpd CLI
    welcome()

    # Read SANCdpd config file and assign values in the fconf dictionary
    conf.readfile()

    # Begin logging to logfile (if logging is set on the config file).
    if conf.fconf["logging"]:
        lg.begin()

    # Check that we have access to a usable SANCdpd database
    dbops.check_db()

    # Load values from reference tables into global variables
    dbops.loadref()

    # Run main menu for the CLI.
    run_menu(['main'])

    # When run_menu returns, we're done
    return 0


###############################################################################

if __name__ == '__main__':
    startcli()
