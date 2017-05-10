users
=====

``add_to_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users add_to_group [OPTIONS] GROUP USER

**Help**

Add a user to a group

**Options**::


      --help  Show this message and exit.
    

``create_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users create_user [OPTIONS] EMAIL FIRST_NAME LAST_NAME PASSWORD

**Help**

Create a new user

**Options**::


      --role TEXT      User's default role, one of "admin" or "user"
      --metadata TEXT  User metadata
      --help           Show this message and exit.
    

``delete_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users delete_user [OPTIONS] USER

**Help**

Delete a user

**Options**::


      --help  Show this message and exit.
    

``get_organism_permissions`` command
------------------------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users get_organism_permissions [OPTIONS] USER

**Help**

Display a user's organism permissions

**Options**::


      --help  Show this message and exit.
    

``get_users`` command
---------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users get_users [OPTIONS]

**Help**

Get all users known to this Apollo instance

**Options**::


      --help  Show this message and exit.
    

``remove_from_group`` command
-----------------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users remove_from_group [OPTIONS] GROUP USER

**Help**

Remove a user from a group

**Options**::


      --help  Show this message and exit.
    

``show_user`` command
---------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users show_user [OPTIONS] USER

**Help**

Get a specific user

**Options**::


      --help  Show this message and exit.
    

``update_organism_permissions`` command
---------------------------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users update_organism_permissions [OPTIONS] USER ORGANISM

**Help**

Update the permissions of a user on a specified organism

**Options**::


      --administrate  Grants administrative privileges
      --write         Grants write privileges
      --export        Grants export privileges
      --read          Grants read privileges
      --help          Show this message and exit.
    

``update_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users``.

**Usage**::

    arrow users update_user [OPTIONS] EMAIL FIRST_NAME LAST_NAME PASSWORD

**Help**

Update an existing user

**Options**::


      --metadata TEXT  User metadata
      --help           Show this message and exit.
    
