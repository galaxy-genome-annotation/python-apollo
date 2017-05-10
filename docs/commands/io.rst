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


**Output**::


[CURRENTLY BROKEN] Download pre-prepared data by UUID

Output:

a dictionary
   
    
**Options**::


      --output_format TEXT  Output format of the data, either "gzip" or "text"
                            [default: gzip]
      -h, --help            Show this message and exit.
    

``write_downloadable`` command
------------------------------

This section is auto-generated from the help text for the arrow command
``io write_downloadable``.

**Usage**::

    arrow io write_downloadable [OPTIONS] ORGANISM

**Help**

Prepare a download for an organism


**Output**::


Prepare a download for an organism

Output:

a dictionary containing download information
   
    
**Options**::


      --export_type TEXT    Export type. Choices: FASTA, GFF3  [default: FASTA]
      --seq_type TEXT       Export selection. Choices: peptide, cds, cdna, genomic
                            [default: peptide]
      --export_format TEXT  Export format, either gzip or text  [default: text]
      --export_gff3_fasta   Export reference sequence when exporting GFF3
                            annotations.
      --sequences TEXT      Names of references sequences to add (default is all)
      -h, --help            Show this message and exit.
    

``write_text`` command
----------------------

This section is auto-generated from the help text for the arrow command
``io write_text``.

**Usage**::

    arrow io write_text [OPTIONS] ORGANISM

**Help**

Download or prepare a download for an organism


**Output**::


Download or prepare a download for an organism

Output:

the exported data
   
    
**Options**::


      --export_type TEXT    Export type. Choices: FASTA, GFF3  [default: FASTA]
      --seq_type TEXT       Export selection. Choices: peptide, cds, cdna, genomic
                            [default: peptide]
      --export_format TEXT  Export format, either gzip or text  [default: text]
      --export_gff3_fasta   Export reference sequence when exporting GFF3
                            annotations.
      --sequences TEXT      Names of references sequences to add (default is all)
      -h, --help            Show this message and exit.
    
