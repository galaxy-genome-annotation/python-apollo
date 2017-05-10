users
=====

``add_to_group`` command
------------------------

This section is auto-generated from the help text for the arrow command
``users add_to_group``.

**Usage**::

    arrow users add_to_group [OPTIONS] GROUP USER

**Help**

Add a user to a group

Output:

 an empty dictionary
    

**Output**::


    
           an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``create_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users create_user``.

**Usage**::

    arrow users create_user [OPTIONS] EMAIL FIRST_NAME LAST_NAME PASSWORD

**Help**

Create a new user

Output:

 an empty dictionary
    

**Output**::


    
           an empty dictionary
    
**Options**::


      --role TEXT      User's default role, one of "admin" or "user"
      --metadata TEXT  User metadata
      -h, --help       Show this message and exit.
    

``delete_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users delete_user``.

**Usage**::

    arrow users delete_user [OPTIONS] USER

**Help**

Delete a user

Output:

 an empty dictionary
    

**Output**::


    
           an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_organism_permissions`` command
------------------------------------

This section is auto-generated from the help text for the arrow command
``users get_organism_permissions``.

**Usage**::

    arrow users get_organism_permissions [OPTIONS] USER

**Help**

Display a user's organism permissions

Output:

 a dictionary containing user's organism permissions
    

**Output**::


    
           a dictionary containing user's organism permissions
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_users`` command
---------------------

This section is auto-generated from the help text for the arrow command
``users get_users``.

**Usage**::

    arrow users get_users [OPTIONS]

**Help**

Get all users known to this Apollo instance

Output:

 list of user info dictionaries
    

**Output**::


    
           list of user info dictionaries
    
**Options**::


      -h, --help  Show this message and exit.
    

``remove_from_group`` command
-----------------------------

This section is auto-generated from the help text for the arrow command
``users remove_from_group``.

**Usage**::

    arrow users remove_from_group [OPTIONS] GROUP USER

**Help**

Remove a user from a group

Output:

 an empty dictionary
    

**Output**::


    
           an empty dictionary
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_user`` command
---------------------

This section is auto-generated from the help text for the arrow command
``users show_user``.

**Usage**::

    arrow users show_user [OPTIONS] USER

**Help**

Get a specific user

Output:

 a dictionary containing user information
    

**Output**::


    
           a dictionary containing user information
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_organism_permissions`` command
---------------------------------------

This section is auto-generated from the help text for the arrow command
``users update_organism_permissions``.

**Usage**::

    arrow users update_organism_permissions [OPTIONS] USER ORGANISM

**Help**

Update the permissions of a user on a specified organism

Output:

 a dictionary containing user's organism permissions
    

**Output**::


    
           a dictionary containing user's organism permissions
    
**Options**::


      --administrate  Grants administrative privileges
      --write         Grants write privileges
      --export        Grants export privileges
      --read          Grants read privileges
      -h, --help      Show this message and exit.
    

``update_user`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``users update_user``.

**Usage**::

    arrow users update_user [OPTIONS] EMAIL FIRST_NAME LAST_NAME PASSWORD

**Help**

Update an existing user

Output:

 a dictionary containing user information
    

**Output**::


    
           a dictionary containing user information
    
**Options**::


      --metadata TEXT  User metadata
      -h, --help       Show this message and exit.
    
