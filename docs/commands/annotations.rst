annotations
===========

This section is auto-generated from the help text for the arrow command
``annotations``.


``add_attribute`` command
-------------------------

**Usage**::

    arrow annotations add_attribute [OPTIONS] FEATURE_ID ATTRIBUTE_KEY

**Help**

Add an attribute to a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``add_comment`` command
-----------------------

**Usage**::

    arrow annotations add_comment [OPTIONS] FEATURE_ID

**Help**

Set a feature's description


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --comments TEXT  Feature comments
      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``add_feature`` command
-----------------------

**Usage**::

    arrow annotations add_feature [OPTIONS]

**Help**

Add a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --feature TEXT   Feature information
      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``add_transcript`` command
--------------------------

**Usage**::

    arrow annotations add_transcript [OPTIONS]

**Help**

[UNTESTED] Add a transcript to a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --transcript TEXT   Transcript data
      --suppress_history  Suppress the history of this operation
      --suppress_events   Suppress instant update of the user interface
      --organism TEXT     Organism Common Name
      --sequence TEXT     Sequence Name
      -h, --help          Show this message and exit.
    

``delete_attribute`` command
----------------------------

**Usage**::

    arrow annotations delete_attribute [OPTIONS] FEATURE_ID ATTRIBUTE_KEY

**Help**

Delete an attribute from a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``delete_feature`` command
--------------------------

**Usage**::

    arrow annotations delete_feature [OPTIONS] FEATURE_ID

**Help**

Delete a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``delete_sequence_alteration`` command
--------------------------------------

**Usage**::

    arrow annotations delete_sequence_alteration [OPTIONS] FEATURE_ID

**Help**

[UNTESTED] Delete a specific feature alteration


**Output**


A list of sequence alterations(?)
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``duplicate_transcript`` command
--------------------------------

**Usage**::

    arrow annotations duplicate_transcript [OPTIONS] TRANSCRIPT_ID

**Help**

Duplicate a transcripte


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``flip_strand`` command
-----------------------

**Usage**::

    arrow annotations flip_strand [OPTIONS] FEATURE_ID

**Help**

Flip the strand of a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``get_comments`` command
------------------------

**Usage**::

    arrow annotations get_comments [OPTIONS] FEATURE_ID

**Help**

Get a feature's comments


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``get_feature_sequence`` command
--------------------------------

**Usage**::

    arrow annotations get_feature_sequence [OPTIONS] FEATURE_ID

**Help**

[CURRENTLY BROKEN] Get the sequence of a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``get_features`` command
------------------------

**Usage**::

    arrow annotations get_features [OPTIONS]

**Help**

Get the features for an organism / sequence


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``get_gff3`` command
--------------------

**Usage**::

    arrow annotations get_gff3 [OPTIONS] FEATURE_ID

**Help**

Get the GFF3 associated with a feature


**Output**


GFF3 text content
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``get_search_tools`` command
----------------------------

**Usage**::

    arrow annotations get_search_tools [OPTIONS]

**Help**

Get the search tools available


**Output**


dictionary containing the search tools and their metadata. E.g.::
       {
           "sequence_search_tools": {
               "blat_prot": {
                   "name": "Blat protein",
                   "search_class": "org.bbop.apollo.sequence.search.blat.BlatCommandLineProteinToNucleotide",
                   "params": "",
                   "search_exe": "/usr/local/bin/blat"
               },
               "blat_nuc": {
                   "name": "Blat nucleotide",
                   "search_class": "org.bbop.apollo.sequence.search.blat.BlatCommandLineNucleotideToNucleotide",
                   "params": "",
                   "search_exe": "/usr/local/bin/blat"
               }
           }
       }
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_sequence_alterations`` command
------------------------------------

**Usage**::

    arrow annotations get_sequence_alterations [OPTIONS]

**Help**

[UNTESTED] Get all of the sequence's alterations


**Output**


A list of sequence alterations(?)
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``merge_exons`` command
-----------------------

**Usage**::

    arrow annotations merge_exons [OPTIONS] EXON_A EXON_B

**Help**

Merge two exons


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_boundaries`` command
--------------------------

**Usage**::

    arrow annotations set_boundaries [OPTIONS] FEATURE_ID START END

**Help**

Set the boundaries of a genomic feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_description`` command
---------------------------

**Usage**::

    arrow annotations set_description [OPTIONS] FEATURE_ID DESCRIPTION

**Help**

Set a feature's description


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_longest_orf`` command
---------------------------

**Usage**::

    arrow annotations set_longest_orf [OPTIONS] FEATURE_ID

**Help**

Automatically pick the longest ORF in a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_name`` command
--------------------

**Usage**::

    arrow annotations set_name [OPTIONS] FEATURE_ID NAME

**Help**

Set a feature's name


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_readthrough_stop_codon`` command
--------------------------------------

**Usage**::

    arrow annotations set_readthrough_stop_codon [OPTIONS] FEATURE_ID

**Help**

Set the feature to read through the first encountered stop codon


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_sequence`` command
------------------------

**Usage**::

    arrow annotations set_sequence [OPTIONS] ORGANISM SEQUENCE

**Help**

Set the sequence for subsequent requests. Mostly used in client scripts to avoid passing the sequence and organism on every function call.


**Output**


None
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``set_status`` command
----------------------

**Usage**::

    arrow annotations set_status [OPTIONS] FEATURE_ID STATUS

**Help**

Set a feature's description


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_symbol`` command
----------------------

**Usage**::

    arrow annotations set_symbol [OPTIONS] FEATURE_ID SYMBOL

**Help**

Set a feature's description


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_translation_end`` command
-------------------------------

**Usage**::

    arrow annotations set_translation_end [OPTIONS] FEATURE_ID END

**Help**

Set a feature's end


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``set_translation_start`` command
---------------------------------

**Usage**::

    arrow annotations set_translation_start [OPTIONS] FEATURE_ID START

**Help**

Set the translation start of a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    

``update_attribute`` command
----------------------------

**Usage**::

    arrow annotations update_attribute [OPTIONS] FEATURE_ID ATTRIBUTE_KEY

**Help**

Delete an attribute from a feature


**Output**


A standard apollo feature dictionary ({"features": [{...}]})
   
    
**Options**::


      --organism TEXT  Organism Common Name
      --sequence TEXT  Sequence Name
      -h, --help       Show this message and exit.
    
