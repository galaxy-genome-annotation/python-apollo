groups
======

``create_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``groups create_group``.

**Usage**::

    arrow groups create_group [OPTIONS] NAME

**Help**

Create a new group


**Output**::


Create a new group

Output:

Group information dictionary
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``groups delete_group``.

**Usage**::

    arrow groups delete_group [OPTIONS] GROUP

**Help**

Delete a group


**Output**::


Delete a group

Output:

an empty dictionary
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_groups`` command
----------------------

This section is auto-generated from the help text for the arrow command
``groups get_groups``.

**Usage**::

    arrow groups get_groups [OPTIONS]

**Help**

Get all the groups


**Output**::


Get all the groups

Output:

list of a dictionaries containing group information
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_organism_permissions`` command
------------------------------------

This section is auto-generated from the help text for the arrow command
``groups get_organism_permissions``.

**Usage**::

    arrow groups get_organism_permissions [OPTIONS] GROUP

**Help**

Get the group's organism permissions


**Output**::


Get the group's organism permissions

Output:

a list containing organism permissions (if any)
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_group`` command
----------------------

This section is auto-generated from the help text for the arrow command
``groups show_group``.

**Usage**::

    arrow groups show_group [OPTIONS] GROUP_ID

**Help**

Get information about a group


**Output**::


Get information about a group

Output:

a dictionary containing group information
   
    
**Options**::


      --group INTEGER  Group ID Number
      -h, --help       Show this message and exit.
    

``update_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``groups update_group``.

**Usage**::

    arrow groups update_group [OPTIONS] GROUP_ID NEW_NAME

**Help**

Update the name of a group


**Output**::


Update the name of a group

Output:

a dictionary containing group information
   
    
**Options**::


      --group INTEGER  group ID number
      -h, --help       Show this message and exit.
    

``update_membership`` command
-----------------------------

This section is auto-generated from the help text for the arrow command
``groups update_membership``.

**Usage**::

    arrow groups update_membership [OPTIONS] GROUP_ID

**Help**

Update the group's membership


**Output**::


Update the group's membership

Output:

dictionary of group information
   
    
**Options**::


      --users TEXT  List of emails
      -h, --help    Show this message and exit.
    

``update_organism_permissions`` command
---------------------------------------

This section is auto-generated from the help text for the arrow command
``groups update_organism_permissions``.

**Usage**::

    arrow groups update_organism_permissions [OPTIONS] GROUP ORGANISM_NAME

**Help**

Update the group's permissions on an organism


**Output**::


Update the group's permissions on an organism

Output:

list of group organism permissions
   
    
**Options**::


      --administrate  Should the group have administrate privileges
      --write         Should the group have write privileges
      --read          Should the group have read privileges
      --export        Should the group have export privileges
      -h, --help      Show this message and exit.
    
