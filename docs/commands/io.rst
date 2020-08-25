io
==

This section is auto-generated from the help text for the arrow command
``io``.


``download`` command
--------------------

**Usage**::

    arrow io download [OPTIONS] UUID

**Help**

Download pre-prepared data by UUID


**Output**


    The downloaded content
    
**Options**::


      --output_format TEXT  Output format of the data, either "gzip" or "text"
                            [default: gzip]
    
      -h, --help            Show this message and exit.
    

``write_downloadable`` command
------------------------------

**Usage**::

    arrow io write_downloadable [OPTIONS] ORGANISM

**Help**

Prepare a download for an organism


**Output**


    a dictionary containing download information
    
**Options**::


      --export_type TEXT    Export type. Choices: FASTA, GFF3, VCF  [default: FASTA]
      --seq_type TEXT       Export selection. Choices: peptide, cds, cdna, genomic
                            [default: peptide]
    
      --export_format TEXT  Export format, either gzip or text  [default: text]
      --export_gff3_fasta   Export reference sequence when exporting GFF3
                            annotations.
    
      --sequences TEXT      Names of references sequences to add (default is all)
      --region TEXT         Region to export in form sequence:min..max e.g.,
                            chr3:1001..1034
    
      -h, --help            Show this message and exit.
    

``write_text`` command
----------------------

**Usage**::

    arrow io write_text [OPTIONS] ORGANISM

**Help**

[DEPRECATED, use write_downloadable] Download or prepare a download for an organism


**Output**


    the exported data
    
**Options**::


      --export_type TEXT    Export type. Choices: FASTA, GFF3, VCF  [default: FASTA]
      --seq_type TEXT       Export selection. Choices: peptide, cds, cdna, genomic
                            [default: peptide]
    
      --export_format TEXT  Export format, either gzip or text  [default: text]
      --export_gff3_fasta   Export reference sequence when exporting GFF3
                            annotations.
    
      --sequences TEXT      Names of references sequences to add (default is all)
      --region TEXT         Region to export in form sequence:min..max e.g.,
                            chr3:1001..1034
    
      -h, --help            Show this message and exit.
    
