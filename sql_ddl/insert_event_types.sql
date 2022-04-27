/***************************************************************************** 
insert_event_types.sql

This file contains INSERT statements to add the standard values into the 
following reference tables:
   - event_type
   - event_type_outcome

*****************************************************************************/


-- Tell the SQLite engine to enable foreign keys for the following statements
PRAGMA foreign_keys = ON;


INSERT INTO event_type 
    (event_type_code, event_name, event_category_code, LC_event_term)
VALUES
    ("STBKP", "Perform backup",         "STORG", "replication"),
    ("STMIG", "Storage migration",      "STORG", "refreshment"),
    ("QRNTN", "Enter quarantine",       "BGADM", "quarantine"),
    ("UNQRN", "Exit quarantine",        "BGADM", "unquarantine"),
    ("VRSSC", "Scan for viruses",       "BGADM", "virus check"),
    ("INGST", "Repository ingest",      "BGADM", "ingestion"),
    ("BGVAL", "Bag validation",         "BGADM", "validation"),
    ("TGCMP", "Tagmanifest comparison", "BGADM", "fixity check"),
    ("CRACC", "Create access copy",     "BGADM", "creation"),
    ("DCRYP", "Decrypt file",           "BGALT", "decryption"),
    ("REDCT", "Perform redaction",      "BGALT", "redaction"),
    ("PRCSS", "Perform processing",     "BGALT", "modification"),
    ("WEEDN", "Perform weeding",        "BGALT", "modification"),
    ("RENFL", "Rename files",           "BGALT", "normalization"),
    ("FLMIG", "File format migration",  "BGALT", "migration"),
    ("VRSRM", "Virus remediation",      "BGALT", "modification"),
    ("BGRGS", "Register bag",           "BGLIN", "metadata extraction"),
    ("BGCRE", "Create bag",             "BGLIN", "information package creation"),
    ("BGREB", "Rebag",                  "BGLIN", "modification"),
    ("BGSPL", "Split bag",              "BGLIN", "information package splitting"),
    ("BGMRG", "Merge bags",             "BGLIN", "information package merging"),
    ("BGDEL", "Delete bag",             "BGLIN", "deletion"),
    ("SCNPI", "Scan for PII",           "OTHER", "forensic feature analysis"),
    ("IDDUP", "Identify duplicate files", "OTHER", "forensic feature analysis"),
    ("IDENC", "Identify encrypted files", "OTHER", "forensic feature analysis"),
    ("IDFLF", "File format identification", "OTHER", "format identification"),
    ("MDUPD", "Metadata update",        "OTHER", "metadata modification");



INSERT INTO event_type_outcome 
    (event_type_code, outcome_code, outcome_name)
VALUES
    ("STBKP", "SUCC", "Success"),
    ("STBKP", "FAIL", "Failure"),
    ("STBKP", "ERR",  "Error"),
    ("STBKP", "PSUC", "Partial success"),
    ("STMIG", "SUCC", "Success"),
    ("STMIG", "FAIL", "Failure"),
    ("STMIG", "ERR",  "Error"),
    ("STMIG", "PSUC", "Partial success"),
    ("QRNTN", "SUCC", "Success"),
    ("UNQRN", "SUCC", "Success"),
    ("VRSSC", "NVIR", "No virus found"),
    ("VRSSC", "VIR",  "Virus found"),
    ("VRSSC", "ERR",  "Error"),
    ("INGST", "SUCC", "Success"),
    ("BGVAL", "VAL",  "Valid"),
    ("BGVAL", "NVAL", "Not valid"),
    ("BGVAL", "ERR",  "Error"),
    ("TGCMP", "SAME", "Same"),
    ("TGCMP", "NSAM", "Not same"),
    ("TGCMP", "ERR",  "Error"),
    ("CRACC", "COMP", "Complete"),
    ("CRACC", "CMER", "Complete with errors"),
    ("CRACC", "ERR",  "Error"),
    ("DCRYP", "SUCC", "Success"),
    ("DCRYP", "ATT",  "Attempted"),
    ("REDCT", "SUCC", "Success"),
    ("PRCSS", "SUCC", "Success"),
    ("WEEDN", "SUCC", "Success"),
    ("RENFL", "SUCC", "Success"),
    ("FLMIG", "SUCC", "Success"),
    ("FLMIG", "ATT",  "Attempted"),
    ("VRSRM", "SUCC", "Success"),
    ("VRSRM", "ATT",  "Attempted"),
    ("BGRGS", "SUCC", "Success"),
    ("BGCRE", "SUCC", "Success"),
    ("BGREB", "SUCC", "Success"),
    ("BGSPL", "SUCC", "Success"),
    ("BGMRG", "SUCC", "Success"),
    ("BGDEL", "SUCC", "Success"),
    ("SCNPI", "COMP", "Complete"),
    ("SCNPI", "CMER", "Complete with errors"),
    ("IDDUP", "COMP", "Complete"),
    ("IDDUP", "CMER", "Complete with errors"),
    ("IDENC", "COMP", "Complete"),
    ("IDENC", "CMER", "Complete with errors"),
    ("IDFLF", "COMP", "Complete"),
    ("IDFLF", "CMER", "Complete with errors"),
    ("MDUPD", "SUCC", "Success");    


