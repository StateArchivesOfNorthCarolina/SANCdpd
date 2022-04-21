# SANCdpd

SANCdpd means _State Archives of North Carolina digital preservation data_.

SANCdpd is an application and database for managing the SANC digital repository and associated digital preservation metadata.

It operates on the files and directories of the digital repository and an SQLite database which records the metadata.


## Installation

- Copy or extract the full SANCdpd directory to a user directory.  

- Create a config file called SANCdpd_config.json.  (See the resources directory for template and an example.)

- Make sure your config file points at a proper SANCdpd SQLite database.

- SANCdpd will check for the config file in the SANCdpd directory (the same directory as this README.md file).


## Usage

$ python3 sancdpd


## License

See the LICENSE file for details.


## Version history

* SANCdpd 0.0.1
    * Project created, 2022-04-20
