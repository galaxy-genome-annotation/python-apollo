io
==

``download`` command
--------------------

This section is auto-generated from the help text for the arrow command
``io download``.

**Usage**::

    arrow io download [OPTIONS] UUID

**Help**

[CURRENTLY BROKEN] Download pre-prepared data by UUID

**Options**::


      --output_format TEXT  Output format of the data, either "gzip" or "text"
      --help                Show this message and exit.
    

``write`` command
-----------------

This section is auto-generated from the help text for the arrow command
``io write``.

**Usage**::

    arrow io write [OPTIONS] ORGANISM

**Help**

Download or prepare a download for an organism

**Options**::


      --export_type TEXT    Export type. Choices: FASTA, GFF3
      --seq_type TEXT       Export selection. Choices: peptide, cds, cdna, genomic
      --export_format TEXT  Export format, either gzip or text
      --output TEXT         Export destination, either file or "text" (i.e.
                            response)
      --export_gff3_fasta   Export reference sequence when exporting GFF3
                            annotations.
      --sequences TEXT      Names of references sequences to add (default is all)
      --help                Show this message and exit.
    
