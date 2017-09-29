cannedcomments
==============

This section is auto-generated from the help text for the arrow command
``cannedcomments``.


``add_comment`` command
-----------------------

**Usage**::

    arrow cannedcomments add_comment [OPTIONS] COMMENT

**Help**

Add a canned comment


**Output**


A dictionnary containing canned comment description
   
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    

``delete_comment`` command
--------------------------

**Usage**::

    arrow cannedcomments delete_comment [OPTIONS] ID_NUMBER

**Help**

Update a canned comment


**Output**


an empty dictionary
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_comments`` command
------------------------

**Usage**::

    arrow cannedcomments get_comments [OPTIONS]

**Help**

Get all canned comments available in this Apollo instance


**Output**


list of canned comment info dictionaries
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_comment`` command
------------------------

**Usage**::

    arrow cannedcomments show_comment [OPTIONS] VALUE

**Help**

Get a specific canned comment


**Output**


A dictionnary containing canned comment description
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_comment`` command
--------------------------

**Usage**::

    arrow cannedcomments update_comment [OPTIONS] ID_NUMBER NEW_VALUE

**Help**

Update a canned comment


**Output**


an empty dictionary
   
    
**Options**::


      --metadata TEXT  Optional metadata
      -h, --help       Show this message and exit.
    
