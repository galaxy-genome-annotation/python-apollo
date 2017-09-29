cannedkeys
==========

This section is auto-generated from the help text for the arrow command
``cannedkeys``.


``add_key`` command
-------------------

**Usage**::

    arrow cannedkeys add_key [OPTIONS] KEY

**Help**

Add a canned key


**Output**


A dictionnary containing canned key description
   
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    

``delete_key`` command
----------------------

**Usage**::

    arrow cannedkeys delete_key [OPTIONS] ID_NUMBER

**Help**

Update a canned key


**Output**


an empty dictionary
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_keys`` command
--------------------

**Usage**::

    arrow cannedkeys get_keys [OPTIONS]

**Help**

Get all canned keys available in this Apollo instance


**Output**


list of canned key info dictionaries
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_key`` command
--------------------

**Usage**::

    arrow cannedkeys show_key [OPTIONS] VALUE

**Help**

Get a specific canned key


**Output**


A dictionnary containing canned key description
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_key`` command
----------------------

**Usage**::

    arrow cannedkeys update_key [OPTIONS] ID_NUMBER NEW_KEY

**Help**

Update a canned key


**Output**


an empty dictionary
   
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    
