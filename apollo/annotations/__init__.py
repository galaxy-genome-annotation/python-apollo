"""
Contains possible interactions with the Apollo's Annotations
"""
from apollo.client import Client


class AnnotationsClient(Client):
    CLIENT_BASE = '/annotationEditor/'

    def _update_data(self, data, organism=None, sequence=None):
        if sequence and organism:
            self.set_sequence(organism, sequence)

        if not hasattr(self, '_extra_data'):
            raise Exception("Please call setSequence first")

        data.update(self._extra_data)
        return data

    def set_sequence(self, organism, sequence):
        """
        Set the sequence for subsequent requests. Mostly used in client scripts
        to avoid passing the sequence and organism on every function call.

        :type organism: str
        :param organism: Organism Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: None
        :return: None
        """
        self._extra_data = {
            'sequence': sequence,
            'organism': organism,
        }

    def set_description(self, feature_id, description, organism=None, sequence=None):
        """
        Set a feature's description

        :type feature_id: str
        :param feature_id: Feature UUID

        :type description: str
        :param description: Feature description

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'description': description,
                }
            ]
        }
        data = self._update_data(data, sequence, organism)
        return self.post('setDescription', data)

    def set_name(self, feature_id, name, organism=None, sequence=None):
        """
        Set a feature's name

        :type feature_id: str
        :param feature_id: Feature UUID

        :type name: str
        :param name: Feature name

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        # TODO
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'name': name,
                }
            ],
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setName', data)

    def set_status(self, feature_id, status, organism=None, sequence=None):
        """
        Set a feature's description

        :type feature_id: str
        :param feature_id: Feature UUID

        :type status: str
        :param status: Feature status

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'status': status,
                }
            ],
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setStatus', data)

    def set_symbol(self, feature_id, symbol, organism=None, sequence=None):
        """
        Set a feature's description

        :type feature_id: str
        :param feature_id: Feature UUID

        :type symbol: str
        :param symbol: Feature symbol

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'symbol': symbol,
                }
            ],
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setSymbol', data)

    def get_comments(self, feature_id, organism=None, sequence=None):
        """
        Get a feature's comments

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                }
            ],
        }
        data = self._update_data(data, organism, sequence)
        return self.post('getComments', data)

    def add_comment(self, feature_id, comments=[], organism=None, sequence=None):
        """
        Set a feature's description

        :type feature_id: str
        :param feature_id: Feature UUID

        :type comments: list
        :param comments: Feature comments

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'comments': comments
                }
            ],
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addComments', data)

    def add_attribute(self, feature_id, attribute_key, attribute_value, organism=None, sequence=None):
        """
        Add an attribute to a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type attribute_key: str
        :param attribute_key: Attribute Key

        :type attribute_value: str
        :param attribute_value: Attribute Value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        This seems to show two attributes being added, but it behaves like those two are one.

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': [
                        {
                            'tag': attribute_key,
                            'value': attribute_value,
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addAttribute', data)

    def delete_attribute(self, feature_id, attribute_key, attribute_value, organism=None, sequence=None):
        """
        Delete an attribute from a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type attribute_key: str
        :param attribute_key: Attribute Key

        :type attribute_value: str
        :param attribute_value: Attribute Value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': [
                        {
                            'tag': attribute_key,
                            'value': attribute_value
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteAttribute', data)

    def update_attribute(self, feature_id, attribute_key, old_value, new_value, organism=None, sequence=None):
        """
        Delete an attribute from a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type attribute_key: str
        :param attribute_key: Attribute Key

        :type old_value: str
        :param old_value: Old attribute value

        :type new_value: str
        :param new_value: New attribute value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'old_non_reserved_properties': [
                        {
                            'tag': attribute_key,
                            'value': old_value,
                        }
                    ],
                    'new_non_reserved_properties': [
                        {
                            'tag': attribute_key,
                            'value': new_value,
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteAttribute', data)

    def add_dbxref(self, feature_id, db, accession, organism=None, sequence=None):
        """
        Add a dbxref to a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type db: str
        :param db: DB Name (e.g. PMID)

        :type accession: str
        :param accession: Accession Value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        This seems to show two attributes being added, but it behaves like those two are one.

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'dbxrefs': [
                        {
                            'db': db,
                            'accession': accession,
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addDbxref', data)

    def delete_dbxref(self, feature_id, db, accession, organism=None, sequence=None):
        """
        Delete a dbxref from a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type db: str
        :param db: DB Name (e.g. PMID)

        :type accession: str
        :param accession: Accession Value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'dbxrefs': [
                        {
                            'db': db,
                            'accession': accession,
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteDbxref', data)

    def update_dbxref(self, feature_id, old_db, old_accession, new_db, new_accession, organism=None, sequence=None):
        """
        Delete a dbxref from a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type old_db: str
        :param old_db: Old DB Name (e.g. PMID)

        :type old_accession: str
        :param old_accession: Old accession Value

        :type new_db: str
        :param new_db: New DB Name (e.g. PMID)

        :type new_accession: str
        :param new_accession: New accession Value

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'old_dbxrefs': [
                        {
                            'db': old_db,
                            'accession': old_accession,
                        }
                    ],
                    'new_dbxrefs': [
                        {
                            'db': new_db,
                            'accession': new_accession,
                        }
                    ]
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteDbxref', data)

    def get_features(self, organism=None, sequence=None):
        """
        Get the features for an organism / sequence

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {}
        data = self._update_data(data, organism, sequence)
        return self.post('getFeatures', data)

    def get_feature_sequence(self, feature_id, organism=None, sequence=None):
        """
        [CURRENTLY BROKEN] Get the sequence of a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        # Choices: peptide, cds, cdna, genomic
        # { "track": "Miro.v2", "features": [ { "uniquename": "714dcda6-2358-467d-855e-f495a82aa154"  }  ], "operation": "get_sequence", "type": "peptide"  }:
        # { "track": "Miro.v2", "features": [ { "uniquename": "714dcda6-2358-467d-855e-f495a82aa154"  }  ], "operation": "get_sequence", "flank": 500, "type": "genomic"  }:
        # This API is not behaving as expected. Wrong documentation?
        data = {
            'type': 'peptide',
            'features': [
                {'uniquename': feature_id}
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('getSequence', data)

    def add_feature(self, feature={}, organism=None, sequence=None):
        """
        Add a feature

        :type feature: dict
        :param feature: Feature information

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """

        data = {
            'features': feature,
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addFeature', data)

    def add_transcript(self, transcript={}, suppress_history=False, suppress_events=False, organism=None, sequence=None):
        """
        [UNTESTED] Add a transcript to a feature

        :type transcript: dict
        :param transcript: Transcript data

        :type suppress_history: bool
        :param suppress_history: Suppress the history of this operation

        :type suppress_events: bool
        :param suppress_events: Suppress instant update of the user interface

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'suppressHistory': suppress_history,
            'suppressEvents': suppress_events,
            'features': [
                transcript
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addTranscript', data)

    # addExon, add/delete/updateComments, addTranscript skipped due to docs

    def duplicate_transcript(self, transcript_id, organism=None, sequence=None):
        """
        Duplicate a transcripte

        :type transcript_id: str
        :param transcript_id: Transcript UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': transcript_id
                }
            ]
        }

        data = self._update_data(data, organism, sequence)
        return self.post('duplicateTranscript', data)

    def set_translation_start(self, feature_id, start, organism=None, sequence=None):
        """
        Set the translation start of a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type start: int
        :param start: Feature start

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [{
                'uniquename': feature_id,
                'location': {
                    'fmin': start
                }
            }]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setTranslationStart', data)

    def set_translation_end(self, feature_id, end, organism=None, sequence=None):
        """
        Set a feature's end

        :type feature_id: str
        :param feature_id: Feature UUID

        :type end: int
        :param end: Feature end

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [{
                'uniquename': feature_id,
                'location': {
                    'fmax': end
                }
            }]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setTranslationEnd', data)

    def set_longest_orf(self, feature_id, organism=None, sequence=None):
        """
        Automatically pick the longest ORF in a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setLongestOrf', data)

    def set_boundaries(self, feature_id, start, end, organism=None, sequence=None):
        """
        Set the boundaries of a genomic feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type start: int
        :param start: Feature start

        :type end: int
        :param end: Feature end

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [{
                'uniquename': feature_id,
                'location': {
                    'fmin': start,
                    'fmax': end,
                }
            }]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setBoundaries', data)

    def set_readthrough_stop_codon(self, feature_id, organism=None, sequence=None):
        """
        Set the feature to read through the first encountered stop codon

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [{
                'uniquename': feature_id,
            }]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('setReadthroughStopCodon', data)

    def get_sequence_alterations(self, organism=None, sequence=None):
        """
        [UNTESTED] Get all of the sequence's alterations

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: list
        :return: A list of sequence alterations(?)
        """
        data = {}
        data = self._update_data(data, organism, sequence)
        return self.post('getSequenceAlterations', data)

    def delete_sequence_alteration(self, feature_id, organism=None, sequence=None):
        """
        [UNTESTED] Delete a specific feature alteration

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: list
        :return: A list of sequence alterations(?)
        """
        data = {
            'features': [{
                'uniquename': feature_id,
            }]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteSequenceAlteration', data)

    def flip_strand(self, feature_id, organism=None, sequence=None):
        """
        Flip the strand of a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('flipStrand', data)

    def merge_exons(self, exon_a, exon_b, organism=None, sequence=None):
        """
        Merge two exons

        :type exon_a: str
        :param exon_a: Feature UUID

        :type exon_b: str
        :param exon_b: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {'uniquename': exon_a},
                {'uniquename': exon_b},
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('mergeExons', data)

    def delete_feature(self, feature_id, organism=None, sequence=None):
        """
        Delete a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('deleteFeature', data)

    def get_search_tools(self):
        """
        Get the search tools available

        :rtype: dict
        :return: dictionary containing the search tools and their metadata.
          For example::

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
        """
        return self.get('getSequenceSearchTools', {})

    def get_gff3(self, feature_id, organism=None, sequence=None):
        """
        Get the GFF3 associated with a feature

        :type feature_id: str
        :param feature_id: Feature UUID

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: str
        :return: GFF3 text content
        """
        data = {
            'features': [
                {
                    'uniquename': feature_id
                }
            ]
        }
        data = self._update_data(data, organism, sequence)
        return self.post('getGff3', data, is_json=False)
