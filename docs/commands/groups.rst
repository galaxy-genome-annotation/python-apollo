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

**Options**::


      --help  Show this message and exit.
    

``delete_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``groups delete_group``.

**Usage**::

    arrow groups delete_group [OPTIONS] GROUP

**Help**

Delete a group

**Options**::


      --help  Show this message and exit.
    

``get_groups`` command
----------------------

This section is auto-generated from the help text for the arrow command
``groups get_groups``.

**Usage**::

    arrow groups get_groups [OPTIONS]

**Help**

Get all the groups

**Options**::


      --help  Show this message and exit.
    

``get_organism_permissions`` command
------------------------------------

This section is auto-generated from the help text for the arrow command
``groups get_organism_permissions``.

**Usage**::

    arrow groups get_organism_permissions [OPTIONS] GROUP

**Help**

Get the group's organism permissions

**Options**::


      --help  Show this message and exit.
    

``show_group`` command
----------------------

This section is auto-generated from the help text for the arrow command
``groups show_group``.

**Usage**::

    arrow groups show_group [OPTIONS] GROUP_ID

**Help**

Get information about a group

**Options**::


      --group INTEGER  Group ID Number
      --help           Show this message and exit.
    

``update_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``groups update_group``.

**Usage**::

    arrow groups update_group [OPTIONS] GROUP_ID NEW_NAME

**Help**

Update the name of a group

**Options**::


      --group INTEGER  group ID number
      --help           Show this message and exit.
    

``update_membership`` command
-----------------------------

This section is auto-generated from the help text for the arrow command
``groups update_membership``.

**Usage**::

    arrow groups update_membership [OPTIONS] GROUP_ID

**Help**

[CURRENTLY_BROKEN] Update the group's membership

**Options**::


      --users TEXT  List of emails
      --help        Show this message and exit.
    

``update_organism_permissions`` command
---------------------------------------

This section is auto-generated from the help text for the arrow command
``groups update_organism_permissions``.

**Usage**::

    arrow groups update_organism_permissions [OPTIONS] GROUP ORGANISM_NAME

**Help**

Update the group's permissions on an organism

**Options**::


      --administrate  Should the group have administrate privileges
      --write         Should the group have write privileges
      --read          Should the group have read privileges
      --export        Should the group have export privileges
      --help          Show this message and exit.
    
