groups
======

This section is auto-generated from the help text for the arrow command
``groups``.


``create_group`` command
------------------------

**Usage**::

    arrow groups create_group [OPTIONS] NAME

**Help**

Create a new group


**Output**


    Group information dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_group`` command
------------------------

**Usage**::

    arrow groups delete_group [OPTIONS] GROUP

**Help**

Delete a group


**Output**


    an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_group_admin`` command
---------------------------

**Usage**::

    arrow groups get_group_admin [OPTIONS] GROUP

**Help**

Get the group's admins


**Output**


    a list containing group admins
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_group_creator`` command
-----------------------------

**Usage**::

    arrow groups get_group_creator [OPTIONS] GROUP

**Help**

Get the group's creator


**Output**


    creator userId
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_groups`` command
----------------------

**Usage**::

    arrow groups get_groups [OPTIONS]

**Help**

Get all the groups


**Output**


    list of a dictionaries containing group information
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_organism_permissions`` command
------------------------------------

**Usage**::

    arrow groups get_organism_permissions [OPTIONS] GROUP

**Help**

Get the group's organism permissions


**Output**


    a list containing organism permissions (if any)
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_group`` command
----------------------

**Usage**::

    arrow groups show_group [OPTIONS] GROUP_ID

**Help**

Get information about a group


**Output**


    a dictionary containing group information
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_group`` command
------------------------

**Usage**::

    arrow groups update_group [OPTIONS] GROUP_ID NEW_NAME

**Help**

Update the name of a group


**Output**


    a dictionary containing group information
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_group_admin`` command
------------------------------

**Usage**::

    arrow groups update_group_admin [OPTIONS] GROUP_ID

**Help**

Update the group's admins


**Output**


    dictionary of group information
    
**Options**::


      --users TEXT  List of emails
      -h, --help    Show this message and exit.
    

``update_membership`` command
-----------------------------

**Usage**::

    arrow groups update_membership [OPTIONS]

**Help**

Update the group's membership


**Output**


    dictionary of group information
    
**Options**::


      --group_id INTEGER  Group ID Number
      --users TEXT        List of emails
      --memberships TEXT  Bulk memberships to update of the form: [ {groupId:
                          <groupId>,users: ["user1", "user2", "user3"]},
                          {groupId:<another-groupId>, users: ["user2", "user8"]}
                          (users and groupId will be ignored)
      -h, --help          Show this message and exit.
    

``update_organism_permissions`` command
---------------------------------------

**Usage**::

    arrow groups update_organism_permissions [OPTIONS] GROUP ORGANISM_NAME

**Help**

Update the group's permissions on an organism


**Output**


    list of group organism permissions
    
**Options**::


      --administrate  Should the group have administrate privileges
      --write         Should the group have write privileges
      --read          Should the group have read privileges
      --export        Should the group have export privileges
      -h, --help      Show this message and exit.
    
