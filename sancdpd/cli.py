"""
This module runs the CLI for SANCdpd.
"""
# Import modules from the Python standard library
import time

# Import other SANCdpd modules
import conf
import logger as lg


# Update the version number as appropriate
VERSION = "0.0.1"


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
    print("*   SANCdpd              *")
    print("*                        *")
    print("*   (ver " + VERSION + ")          *")
    print("*                        *")
    print("**************************")



###############################################################################
# dictionary: menudefs
###############################################################################
# This dictionary defines the menus for the SANCdpd CLI
# The dictionary key is the internal (non-display) menukey for the menu.
# For each menukey, there is a list that defines one menu.
# The first list item is the title (breadcrumb name) of the menu.
# Each addditional list item is a 4-tuple.
# Each 4-tuple includes:
#    - the option's keyboard command (1-3 lowercase alphanumeric characters)
#    - the option's description (for menu display purposes only)
#    - the program's action type: "menu", "proc", "back"
#    - the menu or proc key
#      (which links to other menus or says which procedure to run)
# Notes on ordering:
#    - Within a menu, the order of the options matters.
#    - The order in which menus are defined in the menudefs dictionary does
#      not matter
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
    ("q", "Quit SANCdpd CLI", "proc", "quit")
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
def run_menu(branch=['main']):
    """
    This function handles display and interaction with the CLI menu.
    It takes as its input a non-empty list of menukeys.  The list, from left
    to right, captures the menu navigation depth, and is used for displaying
    navigation breadcrumbs.  The last item in the list is the menukey for
    the current menu to display.

    This function depends on the menudefs dictionary (which is defined globally
    for this module).  All menu content is defined in menudefs.
    This function assumes that menudefs has a particular structure.
    """

    # Create slight pause to make console interaction feel more intuitive
    time.sleep(0.3)

    # Create and print string of navigation breadcrumbs based on the branch
    crumbs = ""
    for menu in branch:
        crumbs += (">> " + menudefs[menu][0] + "  ")
    crumbs += ">>"
    print("")
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

    # Take the appropriate action based on the
    if next_action == "menu":
        run_menu(branch + [action_spec])
    elif next_action == "back":
        run_menu(branch[:-1])
    elif next_action == "proc":
        run_proc(action_spec)


###############################################################################
# function: run_proc
###############################################################################
def run_proc(procname):
    print("Running", procname)



###############################################################################
# function: start_cli
###############################################################################
def startcli():
    """
    This is the first function that should be run for the CLI.
    """
    welcome()
    conf.read()
    lg.begin()
    conf.validate()
    run_menu()


###############################################################################

if __name__ == '__main__':
    startcli()
