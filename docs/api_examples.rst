Examples
--------

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
