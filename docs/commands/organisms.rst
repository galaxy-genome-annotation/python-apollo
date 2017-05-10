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


      --blatdb TEXT   Server-side Blat directory for the organism
      --genus TEXT    Genus
      --species TEXT  Species
      --public        User's email
      -h, --help      Show this message and exit.
    

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

Delete an organim


**Output**


A list of all remaining organisms
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_organisms`` command
-------------------------

**Usage**::

    arrow organisms get_organisms [OPTIONS]

**Help**

Get all organisms


**Output**


Organisms information
   
    
**Options**::


      --common_name TEXT
      --cn TEXT           Optionally filter on common name
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

    arrow organisms show_organism [OPTIONS] ORGANISM_ID

**Help**

Get information about a specific organism. Due to the lack of an API, this call requires fetching the entire list of organisms and iterating through. If you find this painfully slow, please submit a bug report upstream.


**Output**


a dictionary containing the organism's information
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_organism`` command
---------------------------

**Usage**::

    arrow organisms update_organism [OPTIONS] ORGANISM_ID COMMON_NAME

**Help**

Update an organism


**Output**


a dictionary with information about the new organism
   
    
**Options**::


      --blatdb TEXT   Server-side Blat directory for the organism
      --species TEXT  Species
      --genus TEXT    Genus
      --public        User's email
      -h, --help      Show this message and exit.
    
