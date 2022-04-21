A running list of features to implement in the future
=====================================================


# Configuration files


## Check for configuration files in proper OS-specific directories

On a Windows machine, check in C:\Users\YourUserName\AppData\Local\SANCdpd\

On a GNU/Linux machine, check ~yourusername/.config/SANCdpd/


## Migrate the config file format from JSON to TOML or YAML

The only problem with JSON is that it doesn't allow comments.  This makes the config file less user-friendly.  Consider migrating to a different format like TOML or YAML, especially once modules for these formats is included in the Python standard library.




