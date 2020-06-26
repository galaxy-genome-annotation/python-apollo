"""
Contains possible interactions with the Apollo's Annotations
"""
import logging
import sys
import time
from enum import Enum
from timeit import default_timer

from BCBio import GFF

from apollo import util
from apollo.client import Client
from apollo.util import features_to_feature_schema, retry

log = logging.getLogger()


class FeatureType(Enum):
    FEATURE = 1
    TRANSCRIPT = 2


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

    def add_features(self, features=[], organism=None, sequence=None):
        """
        Add a list of feature

        :type features: list
        :param features: Feature information

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """

        data = {
            'features': features,
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addFeature', data)

    def add_feature(self, feature={}, organism=None, sequence=None):
        """
        Add a single feature

        :type feature: dict
        :param feature: Feature information

        :type organism: str
        :param organism: Organism Common Name

        :type sequence: str
        :param sequence: Sequence Name

        :rtype: dict
        :return: A standard apollo feature dictionary ({"features": [{...}]})
        """
        return self.add_features([feature], organism, sequence)

    def add_transcripts(self, transcripts=[],
                        suppress_history=False, suppress_events=False, organism=None,
                        sequence=None
                        ):
        """
        Add a list of transcript annotations

        :type transcripts: list
        :param transcripts: Transcript data

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
        if transcripts is None:
            transcripts = []
        data = {
            'suppressHistory': suppress_history,
            'suppressEvents': suppress_events,
            'features': transcripts
        }
        data = self._update_data(data, organism, sequence)
        return self.post('addTranscript', data)

    def add_transcript(self, transcript={},
                       suppress_history=False, suppress_events=False, organism=None,
                       sequence=None
                       ):
        """
        Add a single transcript annotation

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
        return self.add_transcripts([transcript], suppress_history, suppress_events, organism, sequence)

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

    def load_legacy_gff3(self, organism, gff3, source=None):
        """
        Load a full GFF3 into annotation track (legacy version, kept for compatibility only)

        :type organism: str
        :param organism: Organism Common Name

        :type gff3: str
        :param gff3: GFF3 to load

        :type source: str
        :param source: URL where the input dataset can be found.

        :rtype: str
        :return: Loading report
        """

        sys.stdout.write('# ')
        sys.stdout.write('\t'.join(['Feature ID', 'Apollo ID', 'Success', 'Messages']))
        sys.stdout.write('\n')

        bad_quals = ['date_creation', 'source', 'owner', 'date_last_modified', 'Name', 'ID']

        for rec in GFF.parse(gff3):
            self.set_sequence(organism, rec.id)
            for feature in rec.features:
                # We can only handle genes right now
                if feature.type not in ('gene', 'terminator'):
                    continue
                # Convert the feature into a presentation that Apollo will accept
                feature_data = features_to_feature_schema([feature])
                # TODO: do we handle all top-types here?
                if 'children' in feature_data[0] and any([child['type']['name'] == 'tRNA'
                                                          for child in feature_data[0]['children']]):
                    # We're experiencing a (transient?) problem where gene_001 to
                    # gene_025 will be rejected. Thus, hardcode to a known working
                    # gene name and update later.

                    feature_data[0]['name'] = 'tRNA_000'
                    tRNA_sf = [child for child in feature.sub_features if child.type == 'tRNA'][0]
                    tRNA_type = 'tRNA-' + tRNA_sf.qualifiers.get('Codon', ["Unk"])[0]

                    if 'Name' in feature.qualifiers:
                        if feature.qualifiers['Name'][0].startswith('tRNA-'):
                            tRNA_type = feature.qualifiers['Name'][0]

                    newfeature = self.add_feature(feature_data[0])

                    def func0():
                        self.set_name(
                            newfeature['features'][0]['uniquename'],
                            tRNA_type,
                        )

                    retry(func0)

                    if source:
                        gene_id = newfeature['features'][0]['parent_id']

                        def setSource():
                            self.add_attribute(gene_id, 'DatasetSource', source)

                        retry(setSource)

                    sys.stdout.write('\t'.join([
                        feature.id,
                        newfeature['features'][0]['uniquename'],
                        'success',
                    ]))
                if feature_data[0]['type']['name'] == 'terminator':
                    # We're experiencing a (transient?) problem where gene_001 to
                    # gene_025 will be rejected. Thus, hardcode to a known working
                    # gene name and update later.
                    feature_data[0]['name'] = 'terminator_000'
                    newfeature = self.add_feature(feature_data[0])

                    def func0():
                        self.set_name(
                            newfeature['features'][0]['uniquename'],
                            'terminator'
                        )

                    retry(func0)

                    if source:
                        gene_id = newfeature['features'][0]['parent_id']

                        def setSource():
                            self.add_attribute(gene_id, 'DatasetSource', source)

                        retry(setSource)

                    sys.stdout.write('\t'.join([
                        feature.id,
                        newfeature['features'][0]['uniquename'],
                        'success',
                    ]))
                else:
                    try:
                        # We're experiencing a (transient?) problem where gene_001 to
                        # gene_025 will be rejected. Thus, hardcode to a known working
                        # gene name and update later.
                        feature_data[0]['name'] = 'gene_000'
                        # Create the new feature
                        newfeature = self.add_feature(feature_data[0])
                        # Extract the UUIDs that apollo returns to us
                        mrna_id = newfeature['features'][0]['uniquename']
                        gene_id = newfeature['features'][0]['parent_id']
                        # Sleep to give it time to actually persist the feature. Apollo
                        # is terrible about writing + immediately reading back written
                        # data.
                        time.sleep(1)

                        # Extract CDS feature from the feature data, this will be used
                        # to set the CDS location correctly (apollo currently screwing
                        # this up (2.0.6))
                        min_cds = None
                        max_cds = None

                        for feat in feature_data[0]['children']:
                            # mRNA level
                            for subfeat in feat['children']:
                                # Can be exon or CDS
                                if subfeat['type']['name'] == 'CDS':
                                    if min_cds is None:
                                        min_cds = subfeat['location']['fmin']
                                        max_cds = subfeat['location']['fmax']
                                    else:
                                        min_cds = min(min_cds, subfeat['location']['fmin'])
                                        max_cds = max(max_cds, subfeat['location']['fmax'])
                                if 'children' in subfeat:
                                    for subsubfeat in subfeat['children']:
                                        if subsubfeat['type']['name'] == 'CDS':
                                            if min_cds is None:
                                                min_cds = subsubfeat['location']['fmin']
                                                max_cds = subsubfeat['location']['fmax']
                                            else:
                                                min_cds = min(min_cds, subsubfeat['location']['fmin'])
                                                max_cds = max(max_cds, subsubfeat['location']['fmax'])

                        # Correct the translation start, but with strand specific log
                        if feature_data[0]['location']['strand'] == 1:
                            self.set_translation_start(mrna_id, min(min_cds, max_cds))
                        else:
                            self.set_translation_start(mrna_id, max(min_cds, max_cds) - 1)

                        # Finally we set the name, this should be correct.
                        def func():
                            self.set_name(mrna_id, feature.qualifiers.get('product',
                                                                          feature.qualifiers.get('Name', ["Unknown"]))[
                                0])

                        retry(func)

                        def func():
                            self.set_name(gene_id, feature.qualifiers.get('product',
                                                                          feature.qualifiers.get('Name', ["Unknown"]))[
                                0])

                        retry(func)

                        if source:
                            gene_id = newfeature['features'][0]['parent_id']

                            def setSource():
                                self.add_attribute(gene_id, 'DatasetSource', source)

                            retry(setSource)
                        extra_attr = {}
                        for (key, values) in feature.qualifiers.items():
                            if key in bad_quals:
                                continue

                            if key == 'Note':
                                def func2():
                                    self.add_comments(gene_id, values)

                                retry(func2)
                            else:
                                extra_attr[key] = values

                        for key in extra_attr:
                            def func3():
                                self.add_attribute(gene_id, key, extra_attr[key])

                            retry(func3)

                        sys.stdout.write('\t'.join([
                            feature.id,
                            gene_id,
                            'success',
                        ]))
                    except Exception as e:
                        msg = str(e)
                        if '\n' in msg:
                            msg = msg[0:msg.index('\n')]
                        sys.stdout.write('\t'.join([
                            feature.id,
                            '',
                            'ERROR',
                            msg
                        ]))
                sys.stdout.write('\n')
                sys.stdout.flush()

    def _check_write(self, batch_size, test, new_features_list=[], type=FeatureType.FEATURE, timing=False):
        if len(new_features_list) >= batch_size:
            log.debug("writing out: " + str(new_features_list))
            returned = self._write_features(new_features_list, test, timing, type)

            if 'error' in returned:
                log.error("Error returned by Apollo while loading data: %s" % returned['error'])
                return {top_in['gff_id']: 'error' for top_in in new_features_list}

            elif len(returned):
                # FIXME this can give strange results in case of error while loading some of the features.
                # This expects the order to be preserved. It's the case in Apollo 2.6.0 at least.
                in_ids = [top_in['gff_id'] for top_in in new_features_list]
                return dict(zip(in_ids, returned['features']))

        return {}

    def _write_features(self, new_features_list=None, test=False, timing=False, feature_type=None):

        if not isinstance(feature_type, FeatureType):
            raise TypeError("Feature type must be of type feature type : " + str(feature_type))

        if len(new_features_list) > 0:
            returned_features = {}
            log.debug("Writing " + str(len(new_features_list)) + " features")
            log.debug("Features to write:")
            log.debug(new_features_list)
            if test:
                print("test success " + str(len(new_features_list)) + " features would have been loaded")
            else:
                if timing:
                    start_time = default_timer()
                try:
                    if feature_type == FeatureType.FEATURE:
                        returned_features = self.add_features(new_features_list)
                    elif feature_type == FeatureType.TRANSCRIPT:
                        returned_features = self.add_transcripts(new_features_list)
                    else:
                        raise Exception("Type '" + str(feature_type) + "' is unknown")
                except Exception:
                    e = sys.exc_info()
                    log.error("Error writing: " + str(e))
                    returned_features = {'error': "Error writing: " + str(e)}
                if timing:
                    end_time = default_timer()
                    duration = end_time - start_time
                    avg_duration = duration / len(new_features_list)
                    if len(new_features_list) > 1:
                        print('({:.1f}/{:.2f})'.format(duration, avg_duration))
                    else:
                        print('({:.2f})'.format(duration))

                log.debug("Features returned: ")
                log.debug(returned_features)
            return returned_features
        else:
            log.debug("empty list, no more features to write")
            return {}

    def _get_type(self, rec):
        return rec.features[0].type

    def _get_subfeature_type(self, rec):
        return rec.features[0].type

    def _process_gff_entry(self, rec, source=None, disable_cds_recalculation=False, use_name=False):

        new_feature_list = []
        new_transcript_list = []

        type = self._get_type(rec)
        log.debug("type " + str(type))

        for feature in rec.features:
            feature_data = None
            if type in util.gene_types:
                log.debug("is gene type")
                if len(feature.sub_features) > 0:
                    feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                        disable_cds_recalculation=disable_cds_recalculation)
                    log.debug("output feature data" + str(feature_data))
                    if isinstance(feature_data, list):
                        new_transcript_list += feature_data
                    else:
                        new_transcript_list.append(feature_data)
                else:
                    log.debug("NO sub features, just adding directly")
                    feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                        disable_cds_recalculation=disable_cds_recalculation)
                    log.debug("output feature data" + str(feature_data))
                    new_feature_list.append(feature_data)
            elif type in util.pseudogenes_types:
                feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                    disable_cds_recalculation=disable_cds_recalculation)
                if isinstance(feature_data, list):
                    new_feature_list += feature_data
                else:
                    new_feature_list.append(feature_data)
            elif type in util.coding_transcript_types:
                feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                    disable_cds_recalculation=disable_cds_recalculation)
                new_transcript_list.append(feature_data)
            elif type in util.noncoding_transcript_types:
                log.debug("a non-coding transcript")
                feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                    disable_cds_recalculation=disable_cds_recalculation)
                new_feature_list.append(feature_data)
                log.debug("new feature list " + str(new_feature_list))
            elif type in util.single_level_feature_types:
                feature_data = util.yieldApolloData(feature, use_name=use_name,
                                                    disable_cds_recalculation=disable_cds_recalculation)
                new_feature_list.append(feature_data)
            else:
                log.debug("unknown type " + type + " ")

        return {'top-level': new_feature_list, 'transcripts': new_transcript_list}

    def load_gff3(self, organism, gff3, source=None, batch_size=1,
                  test=False,
                  use_name=False,
                  disable_cds_recalculation=False,
                  timing=False,
                  ):
        """
        Load a full GFF3 into annotation track

        :type organism: str
        :param organism: Organism Common Name

        :type gff3: str
        :param gff3: GFF3 to load

        :type source: str
        :param source: URL where the input dataset can be found.

        :type batch_size: int
        :param batch_size: Size of batches before writing

        :type test: bool
        :param test: Run in dry run mode

        :type use_name: bool
        :param use_name: Use the given name instead of generating one.

        :type disable_cds_recalculation: bool
        :param disable_cds_recalculation: Disable CDS recalculation and instead use the one provided

        :type timing: bool
        :param timing: Output loading performance metrics

        :rtype: str
        :return: Loading report
        """
        organisms = self._wa.organisms.get_organisms()
        org_ids = []
        for org in organisms:
            if organism == org['commonName'] or organism == str(org['id']):
                org_ids.append(org['id'])

        if len(org_ids) == 0:
            raise Exception("Organism name or id not found [" + organism + "]")

        if len(org_ids) > 1:
            raise Exception("More than one organism found for [" + organism + "].  Use an organism ID instead: " + str(
                org_ids))

        total_features_written = 0
        start_timer = default_timer()
        if timing:
            print('Times are in seconds.  If batch-size > 1 then .(total_batch_time/avg_feature_time)')

        all_processed = {'top-level': [], 'transcripts': []}
        loading_status = {}
        for rec in GFF.parse(gff3):
            self.set_sequence(organism, rec.id)
            try:
                log.info("Processing %s with features: %s" % (rec.id, rec.features))
                processed = self._process_gff_entry(rec, source=source,
                                                    disable_cds_recalculation=disable_cds_recalculation,
                                                    use_name=use_name
                                                    )
                all_processed['top-level'].extend(processed['top-level'])
                all_processed['transcripts'].extend(processed['transcripts'])
                total_features_written += 1
                written_top = self._check_write(batch_size, test, all_processed['top-level'], FeatureType.FEATURE, timing)
                written_transcripts = self._check_write(batch_size, test, all_processed['transcripts'], FeatureType.TRANSCRIPT, timing)

                if len(written_top):
                    all_processed['top-level'] = []
                    loading_status = {**loading_status, **written_top}
                if len(written_transcripts):
                    all_processed['transcripts'] = []
                    loading_status = {**loading_status, **written_transcripts}

            except Exception as e:
                msg = str(e)
                if '\n' in msg:
                    msg = msg[0:msg.index('\n')]
                log.error("Failed to load features from %s" % rec.id)

        # Write the rest of things to write (ignore batch_size)
        written_top = self._check_write(0, test, all_processed['top-level'], FeatureType.FEATURE, timing)
        written_transcripts = self._check_write(0, test, all_processed['transcripts'], FeatureType.TRANSCRIPT, timing)

        if len(written_top):
            all_processed['top-level'] = []
            loading_status = {**loading_status, **written_top}
        if len(written_transcripts):
            all_processed['transcripts'] = []
            loading_status = {**loading_status, **written_transcripts}

        log.info("Finished loading")
        if timing:
            end_timer = default_timer()
            duration = end_timer - start_timer
            print(str(duration) + " seconds to write " + str(total_features_written) + " features")
            print("Avg write time (s) per feature: " + str('{:.3f}'.format(duration / total_features_written)))

        return loading_status
