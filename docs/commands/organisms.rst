organisms
=========

This section is auto-generated from the help text for the arrow command
``organisms``.


``add_organism`` command
------------------------

**Usage**::

    arrow organisms add_organism [OPTIONS] COMMON_NAME DIRECTORY

**Help**

Add an organism


**Output**


    a dictionary with information about the new organism
    
**Options**::


      --blatdb TEXT      Server-side path to 2bit index of the genome for Blat
      --genus TEXT       Genus
      --species TEXT     Species
      --public           Should the organism be public or not
      --metadata TEXT    JSON formatted arbitrary metadata
      --suppress_output  Suppress output of all organisms (true / false) (default
                         false)
    
      -h, --help         Show this message and exit.
    

``delete_features`` command
---------------------------

**Usage**::

    arrow organisms delete_features [OPTIONS] ORGANISM_ID

**Help**

Remove features of an organism


**Output**


    an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_organism`` command
---------------------------

**Usage**::

    arrow organisms delete_organism [OPTIONS] ORGANISM_ID

**Help**

Delete an organism


**Output**


    A list of all remaining organisms
    
**Options**::


      --suppress_output  Suppress return of all organisms (true / false) (default
                         false)
    
      -h, --help         Show this message and exit.
    

``get_organism_creator`` command
--------------------------------

**Usage**::

    arrow organisms get_organism_creator [OPTIONS] ORGANISM_ID

**Help**

Get the creator of an organism


**Output**


    a dictionary containing user information
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_organisms`` command
-------------------------

**Usage**::

    arrow organisms get_organisms [OPTIONS]

**Help**

Get all organisms


**Output**


    Organism information
    
**Options**::


      --common_name TEXT  Optionally filter on common name
      -h, --help          Show this message and exit.
    

``get_sequences`` command
-------------------------

**Usage**::

    arrow organisms get_sequences [OPTIONS] ORGANISM_ID

**Help**

Get the sequences for an organism


**Output**


    The set of sequences associated with an organism
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_organism`` command
-------------------------

**Usage**::

    arrow organisms show_organism [OPTIONS] COMMON_NAME

**Help**

Get information about a specific organism.


**Output**


    a dictionary containing the organism's information
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_metadata`` command
---------------------------

**Usage**::

    arrow organisms update_metadata [OPTIONS] ORGANISM_ID METADATA

**Help**

Update the metadata for an existing organism.


**Output**


    An empty, useless dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_organism`` command
---------------------------

**Usage**::

    arrow organisms update_organism [OPTIONS] ORGANISM_ID COMMON_NAME

**Help**

Update an organism


**Output**


    a dictionary with information about the updated organism
    
**Options**::


      --blatdb TEXT          Server-side Blat directory for the organism
      --species TEXT         Species
      --genus TEXT           Genus
      --public               Viewable without login
      --no_reload_sequences  Set this if you don't want Apollo to reload genome
                             sequences (no change in genome sequence)
    
      --suppress_output      Suppress output of all organisms (true / false)
                             (default false)
    
      -h, --help             Show this message and exit.
    
