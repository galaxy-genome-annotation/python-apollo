remote
======

This section is auto-generated from the help text for the arrow command
``remote``.


``add_organism`` command
------------------------

**Usage**::

    arrow remote add_organism [OPTIONS] COMMON_NAME ORGANISM_DATA

**Help**

Add an organism using the remote organism API.


**Output**


    a dictionary with information about the new organism
    
**Options**::


      --blatdb FILENAME               Path to 2bit index of the genome for Blat
                                      (Blat 2bit data can also be in organism_data
                                      in directory 'searchDatabaseData')
      --genus TEXT                    Genus
      --species TEXT                  Species
      --public                        should the organism be public
      --non_default_translation_table INTEGER
                                      The translation table number for the organism
                                      (if different than that of the server's
                                      default)
      --metadata TEXT                 JSON formatted arbitrary metadata
      -h, --help                      Show this message and exit.
    

``add_track`` command
---------------------

**Usage**::

    arrow remote add_track [OPTIONS] ORGANISM_ID TRACK_DATA TRACK_CONFIG

**Help**

Adds a tarball containing track data to an existing organism.


**Output**


    a dictionary with information about all tracks on the organism
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_organism`` command
---------------------------

**Usage**::

    arrow remote delete_organism [OPTIONS] ORGANISM_ID

**Help**

Remove an organism completely.


**Output**


    a dictionary with information about the deleted organism
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_track`` command
------------------------

**Usage**::

    arrow remote delete_track [OPTIONS] ORGANISM_ID TRACK_LABEL

**Help**

Remove a track from an organism


**Output**


    a dictionary with information about the deleted track
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_organism`` command
---------------------------

**Usage**::

    arrow remote update_organism [OPTIONS] ORGANISM_ID ORGANISM_DATA

**Help**

Update an organism using the remote organism API.


**Output**


    a dictionary with information about the updated organism
    
**Options**::


      --blatdb FILENAME      Path to 2bit index of the genome for Blat (Blat 2bit
                             data can also be in organism_data in directory
                             'searchDatabaseData')
      --common_name TEXT     Organism common name
      --genus TEXT           Genus
      --species TEXT         Species
      --public               User's email
      --metadata TEXT        JSON formatted arbitrary metadata
      --no_reload_sequences  Set this if you don't want Apollo to reload genome
                             sequences (no change in genome sequence)
      -h, --help             Show this message and exit.
    

``update_track`` command
------------------------

**Usage**::

    arrow remote update_track [OPTIONS] ORGANISM_ID TRACK_CONFIG

**Help**

Update the configuration of a track that has already been added to the organism. Will not update data for the track.


**Output**


    a dictionary with information about all tracks on the organism
    
**Options**::


      -h, --help  Show this message and exit.
    
