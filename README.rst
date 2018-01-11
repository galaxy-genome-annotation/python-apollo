Apollo API Library
==================

.. image:: https://travis-ci.org/galaxy-genome-annotation/python-apollo.svg?branch=master
    :target: https://travis-ci.org/galaxy-genome-annotation/python-apollo

.. image:: https://readthedocs.org/projects/python-apollo/badge/?version=latest
    :target: http://python-apollo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Apollo is a Python library for interacting with
`WebApollo <https://github.com/gmod/apollo/>`__

Examples
--------

.. code:: python

    from apollo import WebApolloInstance
    wa = WebApolloInstance('https://fqdn/apollo', 'jane.doe@fqdn.edu', 'password')

    orgs = wa.organisms.add_organism(
        "Yeast",
        "/path/to/jbrowse/data",
        genus='Saccharomyces',
        species='cerevisiae',
        public=False
    )

    # Give webapollo a second to process the uploaded organism.
    time.sleep(1)

    # Then add yourself to permission list
    data = wa.users.update_organism_permissions(
        "jane.doe@fqdn.edu",
        "Yeast",
        write=True,
        export=True,
        read=True,
    )

Or with the new Arrow client:

.. code-block:: shell

    $ arrow groups create_group university
    {
        "publicGroup": false,
        "class": "org.bbop.apollo.UserGroup",
        "name": "university",
        "users": null,
        "id": 558319
    }
    # THEN
    $ arrow users get_users | \
        jq '.[] | select(.username | contains("@tamu.edu")) | .username' | \
        xargs -n1 arrow users add_to_group university
    # OR
    $ arrow users get_users | \
        jq '.[] | select(.username | contains("@tamu.edu")) | .username' | \
        paste -s -d',' | \
        xargs arrow group update_membership 558319 --users

History
-------

- 3.0.4
    - `Fixed bug <https://github.com/galaxy-genome-annotation/python-apollo/issues/4>`__ in deleteFeatures (Thanks `@NeillGibson <https://github.com/NeillGibson>`__)
- 3.0.3
    - findAllOrganisms works correctly, client side filtering no longer necessary.
- 3.0.2
    - Patch a bug discovered in io.write, thanks Morgan!
- 3.0
    - "Arrow" CLI utility
    - More pythonic API and many workarounds for Apollo bugs or oddities
    - Complete package restructure
    - Nearly all functions renamed
- 2.0
    - Galaxy Functions
    - TTL Cache to work around Galaxy's behaviour
    - Status and Canned* Clients from `@abretaud <https://github.com/abretaud>`__
- 1.0
    - Initial release

License
-------

Available under the MIT License



Support
-------

This material is based upon work supported by the National Science Foundation under Grant Number (Award 1565146)

