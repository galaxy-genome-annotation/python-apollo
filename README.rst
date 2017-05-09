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

    orgs = wa.organisms.addOrganism(
        "Yeast",
        "/path/to/jbrowse/data",
        genus='Saccharomyces',
        species='cerevisiae',
        public=False
    )

    # Give webapollo a second to process the uploaded organism.
    time.sleep(1)

    # Then add yourself to permission list
    data = wa.users.updateOrganismPermission(
        wa.me, "Yeast",
        write=True,
        export=True,
        read=True,
    )

History
-------

- 2.0
    - Galaxy Functions
    - TTL Cache to work around Galaxy's behaviour
    - Status and Canned* Clients from [@abretaud](https://github.com/abretaud)
- 1.0
    - Initial release

License
-------

Available under the MIT License
