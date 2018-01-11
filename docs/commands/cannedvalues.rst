cannedvalues
============

This section is auto-generated from the help text for the arrow command
``cannedvalues``.


``add_value`` command
---------------------

**Usage**::

    arrow cannedvalues add_value [OPTIONS] VALUE

**Help**

Add a canned value


**Output**


    A dictionnary containing canned value description
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    

``delete_value`` command
------------------------

**Usage**::

    arrow cannedvalues delete_value [OPTIONS] ID_NUMBER

**Help**

Update a canned value


**Output**


    an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_values`` command
----------------------

**Usage**::

    arrow cannedvalues get_values [OPTIONS]

**Help**

Get all canned values available in this Apollo instance


**Output**


    list of canned value info dictionaries
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_value`` command
----------------------

**Usage**::

    arrow cannedvalues show_value [OPTIONS] VALUE

**Help**

Get a specific canned value


**Output**


    A dictionnary containing canned value description
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_value`` command
------------------------

**Usage**::

    arrow cannedvalues update_value [OPTIONS] ID_NUMBER NEW_VALUE

**Help**

Update a canned value


**Output**


    an empty dictionary
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    
