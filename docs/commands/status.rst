status
======

This section is auto-generated from the help text for the arrow command
``status``.


``add_status`` command
----------------------

**Usage**::

    arrow status add_status [OPTIONS] STATUS

**Help**

Add a status value


**Output**


    A dictionnary containing status description
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_status`` command
-------------------------

**Usage**::

    arrow status delete_status [OPTIONS] ID_NUMBER

**Help**

Delete a status


**Output**


    an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_statuses`` command
------------------------

**Usage**::

    arrow status get_statuses [OPTIONS]

**Help**

Get all statuses available in this Apollo instance


**Output**


    list of status info dictionaries
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_status`` command
-----------------------

**Usage**::

    arrow status show_status [OPTIONS] STATUS

**Help**

Get a specific status


**Output**


    A dictionnary containing status description
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_status`` command
-------------------------

**Usage**::

    arrow status update_status [OPTIONS] ID_NUMBER NEW_VALUE

**Help**

Update a status name


**Output**


    an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    
