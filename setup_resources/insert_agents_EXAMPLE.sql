/***************************************************************************** 
insert_agents_EXAMPLE.sql

This file contains INSERT statements to add some agents to the SANCdpd agent
table.

This file can be copied and then edited as appropriate.

Note that this file uses a specific syntax to ensure that timestamps are 
entered with ISO 8601 date format, for maximum compatibility and as specified
by the SANCdpd data dictionary.

The SQLite engine will create a string in ISO 8601 format with the current
dateime, to the second, from this expression:
    STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime'))

*****************************************************************************/


INSERT INTO agent (
    agent_type_code, 
    is_active, 
    agent_name, 
    agent_code, 
    SANC_user_code, 
    created_time,  
    agent_version)
VALUES
('PERSN', True, 'Jamie Patrick-Burns', 'JAPB', 'JAP', STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime')), NULL),
('PERSN', True, 'Owen King', 'OCK', NULL, STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime')), NULL),
('SOFTW', False, 'SANCdpd CLI', NULL, NULL, STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime')), '0.0.1'),
('SOFTW', True, 'SANCdpd CLI', NULL, NULL, STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime')), '0.1.0'),
('ORGZN', True, 'SANC DSS', 'SANCDS', NULL, STRFTIME('%Y-%m-%dT%H:%M:%S',DATETIME('now', 'localtime')), NULL)
;
