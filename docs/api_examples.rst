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
