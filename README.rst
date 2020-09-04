Apollo API Library
==================

.. image:: https://travis-ci.org/galaxy-genome-annotation/python-apollo.svg?branch=master
    :target: https://travis-ci.org/galaxy-genome-annotation/python-apollo

.. image:: https://readthedocs.org/projects/python-apollo/badge/?version=latest
    :target: http://python-apollo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Apollo is a Python library for interacting with
`Apollo <https://github.com/gmod/apollo/>`__. Arrow is its companion CLI tool.

    `for the record <https://gitter.im/galaxy-genome-annotation/Lobby?at=5ebee6c049a1b7318479380d>`__ ... arrow makes working with Apollo SOOO much easier
    — Nathan Dunn, Apollo Developer


Installation
------------

.. code-block:: shell

    pip install apollo

Examples
--------

Example code to create a new organism and add yourself in the permission list:

.. code:: python

    from apollo import ApolloInstance
    wa = ApolloInstance('https://fqdn/apollo', 'jane.doe@fqdn.edu', 'password')

    orgs = wa.organisms.add_organism(
        "Yeast",
        "/path/to/jbrowse/data",
        genus='Saccharomyces',
        species='cerevisiae',
        public=False
    )

    # Give Apollo a second to process the uploaded organism.
    time.sleep(1)

    # Then add yourself to permission list
    data = wa.users.update_organism_permissions(
        "jane.doe@fqdn.edu",
        "Yeast",
        write=True,
        export=True,
        read=True,
    )

If you have already created an Arrow config file (with command `arrow init`),
you can also get an ApolloInstance without writing credentials explicitely:

.. code:: python

    from arrow.apollo import get_apollo_instance
    wa = get_apollo_instance()

Or with the Arrow client:

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

- 4.2.9
    - Bugfix to  update_organism when using suppress_output
- 4.2.8
    - Added --suppress_output to update_organism
- 4.2.7
    - Renamed --return_all option to --suppress_output
- 4.2.6
    - Added --return_all option to add_organism and delete_organism methods
- 4.2.5
    - Prevent from displaying login/password in the logs
- 4.2.4
    - Remove unused dependency
- 4.2.3
    - Fixed `load_gff3` to more accurately load transcripts including the CDS as well as handle non-coding types more accurately.
- 4.2.2
    - Drastically speed up load_gff3
    - `load_gff3` now uses the Apollo `add_transcript` method if it is a gene or mRNA type
    - Added support for all of the current Apollo coding and non-coding types
    - Drop support for Python 2.7
- 4.2.1
    - Fix getting groups by name
    - Add tests for group api
- 4.2
    - Improve user update method
    - Add tests for user api
- 4.1
    - Fix loading attributes from gff3
    - Better handling of genome sequence update, with or without the no_reload_sequences option
- 4.0.1
    - Fix missing file in pypi package, no code change
- 4.0
    - Added support for remote creation/update/deletion of organisms/tracks
    - Added support for adding GFF3 in the annotation track
    - Added tests
- 3.1
    - Added user activate/inactivate
    - Added get_creator for user, group and organisms
    - Added omitEmptyOrganisms to get_users
    - Added support for group admins
    - Added support for bulk group creation/deletion
    - Repaired GFF3/Fasta downloading
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


Development
-----------

The content of docs and arrow directories is automatically generated from the code in the apollo directory.
To regenerate it, install the latest version of the code, then run:


.. code-block:: shell

    make rebuild


License
-------

Available under the MIT License



Support
-------

This material is based upon work supported by the National Science Foundation under Grant Number (Award 1565146)
