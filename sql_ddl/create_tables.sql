/**************************************************************************** 
create_tables.sql

This file consists of SQL data definition statements to create the tables
that compose the SANCdpd data model.
****************************************************************************/

-- Tell the SQLite engine to enable foreign keys for the following statements
PRAGMA foreign_keys = ON;



CREATE TABLE accession (
    accession_id INTEGER PRIMARY KEY AUTOINCREMENT,
    SANC_accession_no VARCHAR(20) NOT NULL UNIQUE,
    accession_desc VARCHAR(100)
);
CREATE TABLE pseudo_accession (
    pseudo_accession_id INTEGER PRIMARY KEY AUTOINCREMENT,
    DSS_pseudo_accession_no VARCHAR(20) NOT NULL UNIQUE,
    pseudo_accession_desc VARCHAR(100) NOT NULL,
    pseudo_accession_explanation VARCHAR(500) NOT NULL
);
CREATE TABLE records_collection (
    records_collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    SANC_bib_record_id VARCHAR(20) NOT NULL UNIQUE,
    records_collection_desc VARCHAR(100)
);
CREATE TABLE item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    SANC_item_no VARCHAR(20) NOT NULL UNIQUE,
    item_desc VARCHAR(100)
);
CREATE TABLE storage (
    storage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    path_root VARCHAR(50) NOT NULL,
    storage_name VARCHAR(50) NOT NULL,
    storage_notes VARCHAR(500),
    in_use BOOLEAN NOT NULL
);
CREATE TABLE bag_family (
    bag_family_id INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE bag (
    bag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bag_family_id INTEGER NOT NULL,
    storage_id INTEGER NOT NULL,
    preservation_path VARCHAR(100) NOT NULL,
    preservation_bag_name VARCHAR(50) NOT NULL,
    SANC_container_id VARCHAR(50) NOT NULL,
    original_bag_name VARCHAR(255) NOT NULL,
    records_collection_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    still_exists BOOLEAN NOT NULL,
    born_digital BOOLEAN NOT NULL,
    preservation_level_code VARCHAR(5),
    preservation_level_explanation VARCHAR(2500),
    processing_status_code VARCHAR(5) NOT NULL,
    processing_notes VARCHAR(500),
    path_records_status VARCHAR(5) NOT NULL,
    path_collection_type VARCHAR(5) NOT NULL,
    path_records_group VARCHAR(20) NOT NULL,
    path_series_no VARCHAR(20),
    path_item_no VARCHAR(20),
    path_accession_no VARCHAR(20) NOT NULL,
    path_accession_no_suffix VARCHAR(4),
    tagmanifest_filename VARCHAR(50),
    tagmanifest_contents VARCHAR(5000) UNIQUE,
    `bag-info_contents` VARCHAR(5000) NOT NULL,
    `bag-info_Bagging-Date` VARCHAR(50),
    `bag-info_digitalContentStructure` VARCHAR(100),
    `bag-info_digitalOriginality` VARCHAR(100),
    payload_files INTEGER NOT NULL,
    payload_bytes BIGINT NOT NULL,
    total_files INTEGER,
    total_bytes BIGINT,
    general_notes VARCHAR(2500),
    FOREIGN KEY (bag_family_id)
        REFERENCES bag_family (bag_family_id),
    FOREIGN KEY (storage_id)
        REFERENCES storage (storage_id),
    FOREIGN KEY (records_collection_id)
        REFERENCES records_collection (records_collection_id),
    FOREIGN KEY (item_id)
        REFERENCES item (item_id)
);
CREATE TABLE bag_from_accession (
    bag_id INTEGER NOT NULL,
    accession_id INTEGER,
    pseudo_accession_id INTEGER,
    PRIMARY KEY (bag_id, accession_id, pseudo_accession_id),
    FOREIGN KEY (bag_id) 
        REFERENCES bag (bag_id),
    FOREIGN KEY (accession_id) 
        REFERENCES accession (accession_id),
    FOREIGN KEY (pseudo_accession_id) 
        REFERENCES pseudo_accession (pseudo_accession_id),
    CHECK (
        ((accession_id IS NOT NULL) AND (pseudo_accession_id IS NULL)) OR
        ((accession_id IS NULL) AND (pseudo_accession_id IS NOT NULL)) ) 
);
CREATE TABLE bag_has_parent_bag (
    child_bag_id INTEGER NOT NULL,
    parent_bag_id INTEGER NOT NULL,
    FOREIGN KEY (child_bag_id)
        REFERENCES bag (bag_id),
    FOREIGN KEY (parent_bag_id)
        REFERENCES bag (bag_id)
);
CREATE TABLE event_type (
    event_type_code VARCHAR(5) PRIMARY KEY,
    event_name VARCHAR(50) NOT NULL UNIQUE,
    event_category_code VARCHAR(5) NOT NULL,
    LC_event_term VARCHAR(100)
);
CREATE TABLE event_type_outcome (
    event_type_code VARCHAR(5) NOT NULL,
    outcome_code VARCHAR(5) NOT NULL,
    outcome_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (event_type_code, outcome_code),
    FOREIGN KEY (event_type_code)
        REFERENCES event_type (event_type_code),
    UNIQUE (event_type_code, outcome_code),
    UNIQUE (event_type_code, outcome_name)
);
CREATE TABLE agent (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_type_code VARCHAR(5) NOT NULL,
    is_active BOOLEAN NOT NULL,
    agent_name VARCHAR(50) NOT NULL,
    agent_code VARCHAR(5) UNIQUE,
    SANC_user_code VARCHAR(20),
    created_time DATETIME NOT NULL,
    deactivated_time DATETIME,
    agent_version VARCHAR(100),
    agent_notes VARCHAR(2500)
);
CREATE TABLE bag_event (
    bag_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bag_id INTEGER NOT NULL,
    event_type_code VARCHAR(5) NOT NULL,
    person_agent_id INTEGER,
    software_agent_id INTEGER,
    hardware_agent_id INTEGER,
    organization_agent_id INTEGER,
    start_time DATETIME,
    end_time DATETIME NOT NULL,
    event_details VARCHAR(2500),
    tools_used VARCHAR(2500),
    outcome_code VARCHAR(5) NOT NULL,
    outcome_details VARCHAR(2500), 
    FOREIGN KEY (bag_id)
        REFERENCES bag (bag_id),
    FOREIGN KEY (event_type_code)
        REFERENCES event_type (event_type_code),
    FOREIGN KEY (person_agent_id)
        REFERENCES agent (agent_id),
    FOREIGN KEY (software_agent_id)
        REFERENCES agent (agent_id),
    FOREIGN KEY (hardware_agent_id)
        REFERENCES agent (agent_id),
    FOREIGN KEY (organization_agent_id)
        REFERENCES agent (agent_id),
    FOREIGN KEY (event_type_code, outcome_code)
        REFERENCES event_type_outcome (event_type_code, outcome_code),
    CHECK (
        (person_agent_id IS NOT NULL) OR
        (software_agent_id IS NOT NULL) OR
        (hardware_agent_id IS NOT NULL) OR
        (organization_agent_id IS NOT NULL) )
);
CREATE TABLE storage_event (
    storage_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    storage_id INTEGER NOT NULL,
    event_type_code VARCHAR(5) NOT NULL,
    start_time DATETIME,
    end_time DATETIME NOT NULL,
    event_details VARCHAR(2500),
    tools_used VARCHAR(2500),
    outcome_code VARCHAR(5) NOT NULL,
    outcome_details VARCHAR(2500),
    FOREIGN KEY (storage_id)
        REFERENCES storage (storage_id),
    FOREIGN KEY (event_type_code)
        REFERENCES event_type (event_type_code),
    FOREIGN KEY (event_type_code, outcome_code)
        REFERENCES event_type_outcome (event_type_code, outcome_code)
);
CREATE TABLE storage_event_by_agent (
    storage_event_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    role_notes VARCHAR(500),
    PRIMARY KEY (storage_event_id, agent_id),
    FOREIGN KEY (storage_event_id) 
        REFERENCES storage_event (storage_event_id),
    FOREIGN KEY (agent_id)
        REFERENCES agent (agent_id)
);



