Arrow
=====

In the latest release of python-apollo, we're happy to introduce
``arrow``, a CLI Apollo tool, very similar to `Galaxy's Parsec
<http://github.com/galaxy-iuc/parsec>`__.

This section will attempt to showcase "real-life" type examples where possible.

Create a Group
--------------

First, we'll create a group for our "university" users:

.. code-block:: shell

    $ arrow groups create_group university

And this returns to us metadata about the group:

.. code-block:: json

    {
        "publicGroup": false,
        "class": "org.bbop.apollo.UserGroup",
        "name": "university",
        "users": null,
        "id": 558319
    }


Now, let's find all users from a certain domain and add them to this group of "university" users. Maybe they need special permissions by default:

.. code-block:: shell

    $ arrow users get_users | \
        jq '.[] | select(.username | contains("@tamu.edu")) | .username' | \
        xargs -n1 arrow users add_to_group university

This will:

1. fetch all of the users
2. select those whose username (their email) contains "@tamu.edu"
3. Return all of the username attributes for those matching users
4. For every user, run ``arrow users add_to_group university <user_id>``

Alternatively you can:

.. code-block:: shell
    $ arrow users get_users | \
        jq '.[] | select(.username | contains("@tamu.edu")) | .username' | \
        paste -s -d',' | \
        xargs arrow group update_membership 558319 --users

1. fetch all of the users
2. select those whose username (their email) contains "@tamu.edu"
3. Return all of the username attributes for those matching users
4. Paste them together with a comma separator
5. Do a single batch update of group membership with the new users
