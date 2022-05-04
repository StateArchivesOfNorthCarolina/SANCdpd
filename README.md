SANCdpd
=======

# Introduction

SANCdpd means _State Archives of North Carolina digital preservation data_.

SANCdpd is an application and database for managing the SANC digital repository and associated digital preservation metadata.

It operates on the files and directories of the digital repository and an SQLite database which records the metadata.


# Installation

- Copy project code
    - Copy or extract the full SANCdpd directory (the directory where you found this readme file) to a directory in the user's space.  This could be anywhere -- the Desktop, the Documents folder, a flash drive, etc.
    - Note:
        - The full project directory (equivalently, the Git repository) is: SANCdpd
        - The Python package is the subdirectory: sancdpd

- Database creation
    - Copy the blank_database.db file from the setup_resources directory to the proper location outside of the SANCdpd project directory.  This could be anywhere -- the Desktop, the Documents folder, a flash drive, etc.
    - Rename that database file as appropriate.  For a development database, an appropriate name might be: SANCdpd_dev.db
    - Open the database with the application of your choice (e.g., DBeaver, DB Browser for SQLite, a custom Python script, etc.).
    - Execute the following scripts in the sql_ddl directory:
        - create_tables.sql
        - create_views.sql  (currently empty)
        - insert_event_types.sql
    - You may also wish to add an initial collection of agents into the database.  For this, you can copy and edit this file in the setup_files directory:
        - insert_agents_EXAMPLE.sql

- Logfile location
    - Create an empty directory somewhere on your computer (not in the SANCdpd project folder, and not in preservation storage) to store log files.  
    - SANCdpd creates a new log file every time it is run.  So, this directory could accumulate a lot of files.  But they're just text files.  So, they won't take up much space (unless the application enters an infinite loop).  

- Config file setup
    - The config file must be a JSON file called: SANCdpd_config.json
    - Use the EXAMPLE and TEMPLATE versions in the setup_resources directory to create/edit your own version as appropriate.  (The meanings of the keys in the file are described in the docstring in the conf.py file.)
    - SANCdpd will search for this config file in the SANCdpd directory (the same directory as this README.md file).
    - Make sure your config file points to the database file you copied above.
    - Make sure your config file points to the logfile directory you created.


# Usage

From the command line, with working directory: SANCdpd/
    $ python3 sancdpd

This will execute the __main__.py module in the sancdpd Python package.

Alternatively, you may run the cli.py module directly. 


# License

See the LICENSE file for details.


## Version milestones

* SANCdpd 0.1.0
    * 2022-05-04
    * Skeletal project handed over from Owen to Jamie   
    * Currently implemented:
        * menu system
        * reading and managing global config data
        * runtime logging system
        * basic database reading and validation
    * Need to be implemented
        * new ingest operational scenario
        * existing data migration operatonal scenario
        * all other operational scenarios
        * other menu items
        
* SANCdpd 0.0.1
    * 2022-04-20
    * Project repository created, 

