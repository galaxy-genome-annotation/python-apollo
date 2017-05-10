organisms
=========

``addOrganism`` command
-----------------------

This section is auto-generated from the help text for the arrow command
``organisms addOrganism``.

**Usage**::

    arrow organisms addOrganism [OPTIONS] COMMONNAME DIRECTORY

**Help**

Warning: Undocumented Method

**Options**::


      --blatdb TEXT
      --species TEXT
      --genus TEXT
      --public TEXT
      --help          Show this message and exit.
    

``add_organism`` command
------------------------

This section is auto-generated from the help text for the arrow command
``organisms add_organism``.

**Usage**::

    arrow organisms add_organism [OPTIONS] COMMON_NAME DIRECTORY

**Help**

Add an organism

**Options**::


      --blatdb TEXT   Server-side Blat directory for the organism
      --genus TEXT    Genus
      --species TEXT  Species
      --public        User's email
      --help          Show this message and exit.
    

``deleteOrganism`` command
--------------------------

This section is auto-generated from the help text for the arrow command
``organisms deleteOrganism``.

**Usage**::

    arrow organisms deleteOrganism [OPTIONS] ORGANISMID

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``deleteOrganismFeatures`` command
----------------------------------

This section is auto-generated from the help text for the arrow command
``organisms deleteOrganismFeatures``.

**Usage**::

    arrow organisms deleteOrganismFeatures [OPTIONS] ORGANISMID

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``delete_features`` command
---------------------------

This section is auto-generated from the help text for the arrow command
``organisms delete_features``.

**Usage**::

    arrow organisms delete_features [OPTIONS] ORGANISM_ID

**Help**

Remove features of an organism

**Options**::


      --help  Show this message and exit.
    

``delete_organism`` command
---------------------------

This section is auto-generated from the help text for the arrow command
``organisms delete_organism``.

**Usage**::

    arrow organisms delete_organism [OPTIONS] ORGANISM_ID

**Help**

Delete an organim

**Options**::


      --help  Show this message and exit.
    

``findAllOrganisms`` command
----------------------------

This section is auto-generated from the help text for the arrow command
``organisms findAllOrganisms``.

**Usage**::

    arrow organisms findAllOrganisms [OPTIONS]

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``findOrganismByCn`` command
----------------------------

This section is auto-generated from the help text for the arrow command
``organisms findOrganismByCn``.

**Usage**::

    arrow organisms findOrganismByCn [OPTIONS] CN

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``findOrganismById`` command
----------------------------

This section is auto-generated from the help text for the arrow command
``organisms findOrganismById``.

**Usage**::

    arrow organisms findOrganismById [OPTIONS] ID_NUMBER

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``getSequencesForOrganism`` command
-----------------------------------

This section is auto-generated from the help text for the arrow command
``organisms getSequencesForOrganism``.

**Usage**::

    arrow organisms getSequencesForOrganism [OPTIONS] COMMONNAME

**Help**

Warning: Undocumented Method

**Options**::


      --help  Show this message and exit.
    

``get_organisms`` command
-------------------------

This section is auto-generated from the help text for the arrow command
``organisms get_organisms``.

**Usage**::

    arrow organisms get_organisms [OPTIONS]

**Help**

Get all organisms

**Options**::


      --common_name TEXT
      --cn TEXT           Optionally filter on common name
      --help              Show this message and exit.
    

``get_sequences`` command
-------------------------

This section is auto-generated from the help text for the arrow command
``organisms get_sequences``.

**Usage**::

    arrow organisms get_sequences [OPTIONS] ORGANISM_ID

**Help**

Get the sequences for an organism

**Options**::


      --help  Show this message and exit.
    

``show_organism`` command
-------------------------

This section is auto-generated from the help text for the arrow command
``organisms show_organism``.

**Usage**::

    arrow organisms show_organism [OPTIONS] ORGANISM_ID

**Help**

Get information about a specific organism. Due to the lack of an API, this call requires fetching the entire list of organisms and iterating through. If you find this painfully slow, please submit a bug report upstream.

**Options**::


      --help  Show this message and exit.
    

``updateOrganismInfo`` command
------------------------------

This section is auto-generated from the help text for the arrow command
``organisms updateOrganismInfo``.

**Usage**::

    arrow organisms updateOrganismInfo [OPTIONS] ORGANISM_ID COMMON_NAME

**Help**

Update an organism

**Options**::


      --blatdb TEXT   Server-side Blat directory for the organism
      --species TEXT  Species
      --genus TEXT    Genus
      --public        User's email
      --help          Show this message and exit.
    

``update_organism`` command
---------------------------

This section is auto-generated from the help text for the arrow command
``organisms update_organism``.

**Usage**::

    arrow organisms update_organism [OPTIONS] ORGANISM_ID COMMON_NAME

**Help**

Update an organism

**Options**::


      --blatdb TEXT   Server-side Blat directory for the organism
      --species TEXT  Species
      --genus TEXT    Genus
      --public        User's email
      --help          Show this message and exit.
    
