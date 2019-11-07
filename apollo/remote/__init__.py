"""
Contains possible interactions with the Apollo Organisms Module
"""
import json

from apollo.client import Client


class RemoteClient(Client):
    CLIENT_BASE = '/organism/'

    def add_organism(self, common_name, organism_data, blatdb=None, genus=None,
                     species=None, public=None, non_default_translation_table=None, metadata=None):
        """
        Add an organism using the remote organism API.

        The recommended structure for the genome data tarball is as follows::

            names/
            names/root.json
            searchDatabaseData/blat_db.2bit
            seq/
            seq/fba/
            seq/fba/da8/
            seq/fba/da8/f3/
            seq/fba/da8/f3/Mijalis-0.txt
            seq/fba/da8/f3/Mijalis-1.txt
            seq/fba/da8/f3/Mijalis-2.txt
            seq/fba/da8/f3/Mijalis-3.txt
            seq/fba/da8/f3/Mijalis-4.txt
            seq/refSeqs.json
            tracks/
            trackList.json
            tracks.conf

        The genome name / hashed directories below the seq folder will
        obviously be specific to your organism.

        :type common_name: str
        :param common_name: Organism common name

        :type organism_data: file
        :param organism_data: .tar.gz or .zip archive containing the data directory.

        :type blatdb: file
        :param blatdb: Path to 2bit index of the genome for Blat (Blat 2bit data can also be in organism_data in directory 'searchDatabaseData')

        :type genus: str
        :param genus: Genus

        :type species: str
        :param species: Species

        :type public: bool
        :param public: should the organism be public

        :type non_default_translation_table: int
        :param non_default_translation_table: The translation table number for
                                              the organism (if different than
                                              that of the server's default)

        :type metadata: str
        :param metadata: JSON formatted arbitrary metadata

        :rtype: dict
        :return: a dictionary with information about the new organism
        """
        data = {
            'commonName': common_name,
        }

        files = {'organismData': organism_data}

        if blatdb is not None:
            files['searchDatabaseData'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species
        if metadata is not None:
            if isinstance(metadata, dict):
                # Apollo wants a string
                metadata = json.dumps(metadata)
            data['metadata'] = metadata
        if public is not None:
            data['publicMode'] = public

        response = self.post('addOrganismWithSequence', list(data.items()), files=files, autoconvert_to_json=False)
        if 'error' in response:
            return response

        return [x for x in response if x['commonName'] == common_name]

    def update_organism(self, organism_id, organism_data, blatdb=None, common_name=None,
                        genus=None, species=None, public=None, metadata=None, no_reload_sequences=False):
        """
        Update an organism using the remote organism API.

        The recommended structure for the genome data tarball is as follows::

            names/
            names/root.json
            searchDatabaseData/blat_db.2bit
            seq/
            seq/fba/
            seq/fba/da8/
            seq/fba/da8/f3/
            seq/fba/da8/f3/Mijalis-0.txt
            seq/fba/da8/f3/Mijalis-1.txt
            seq/fba/da8/f3/Mijalis-2.txt
            seq/fba/da8/f3/Mijalis-3.txt
            seq/fba/da8/f3/Mijalis-4.txt
            seq/refSeqs.json
            tracks/
            trackList.json
            tracks.conf

        The genome name / hashed directories below the seq folder will
        obviously be specific to your organism.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type organism_data: file
        :param organism_data: .tar.gz or .zip archive containing the data directory.

        :type blatdb: file
        :param blatdb: Path to 2bit index of the genome for Blat (Blat 2bit data can also be in organism_data in directory 'searchDatabaseData')

        :type common_name: str
        :param common_name: Organism common name

        :type genus: str
        :param genus: Genus

        :type species: str
        :param species: Species

        :type public: bool
        :param public: User's email

        :type metadata: str
        :param metadata: JSON formatted arbitrary metadata

        :type no_reload_sequences: bool
        :param no_reload_sequences: Set this if you don't want Apollo to reload genome sequences (no change in genome sequence)

        :rtype: dict
        :return: a dictionary with information about the updated organism
        """
        data = {
            'id': organism_id,
            'noReloadSequences': no_reload_sequences,
        }

        files = {'organismData': organism_data}

        if blatdb is not None:
            files['searchDatabaseData'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species
        if common_name is not None:
            data['name'] = common_name
        if metadata is not None:
            if isinstance(metadata, dict):
                # Apollo wants a string
                metadata = json.dumps(metadata)
            data['metadata'] = metadata
        if public is not None:
            data['publicMode'] = public

        response = self.post('updateOrganismInfo', list(data.items()), files=files, autoconvert_to_json=False)
        if 'error' in response:
            return response

        for org in response:
            if str(org['id']) == organism_id:
                return org

        return response

    def delete_organism(self, organism_id):
        """
        Remove an organism completely.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: dict
        :return: a dictionary with information about the deleted organism
        """
        data = {
            'organism': organism_id,
        }

        response = self.post('deleteOrganismWithSequence', data)
        return response

    def add_track(self, organism_id, track_data, track_config):
        """
        Adds a tarball containing track data to an existing organism.

        The recommended structure for your track data tarball is as follows::

            tracks/testing2/
            tracks/testing2/Mijalis/
            tracks/testing2/Mijalis/hist-2000-0.json
            tracks/testing2/Mijalis/lf-1.json
            tracks/testing2/Mijalis/lf-2.json
            tracks/testing2/Mijalis/lf-3.json
            tracks/testing2/Mijalis/names.txt
            tracks/testing2/Mijalis/trackData.json

        And an example of the track_config supplied at the same time::

            {
                "key": "Some human-readable name",
                "label": "my-cool-track",
                "storeClass": "JBrowse/Store/SeqFeature/NCList",
                "type": "FeatureTrack",
                "urlTemplate": "tracks/testing2/{refseq}/trackData.json"
            }

        This is only the recommended structure, other directory structures /
        parameter combinations may work but were not tested by the
        python-apollo author who wrote this documentation.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_data: file
        :param track_data: .tar.gz or .zip archive containing the <track> directory.

        :type track_config: dict
        :param track_config: Track configuration

        :rtype: dict
        :return: a dictionary with information about all tracks on the organism
        """
        data = {
            'organism': organism_id,
            'trackConfig': json.dumps(track_config),
        }

        response = self.post('addTrackToOrganism', list(data.items()), files={'trackData': track_data}, autoconvert_to_json=False)
        return response

    def update_track(self, organism_id, track_config):
        """
        Update the configuration of a track that has already been added to the
        organism. Will not update data for the track.

        And an example of the track_config supplied::

            {
                "key": "Some human-readable name",
                "label": "my-cool-track",
                "storeClass": "JBrowse/Store/SeqFeature/NCList",
                "type": "FeatureTrack",
                "urlTemplate": "tracks/testing2/{refseq}/trackData.json"
            }

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_config: dict
        :param track_config: Track configuration

        :rtype: dict
        :return: a dictionary with information about all tracks on the organism
        """
        data = {
            'organism': organism_id,
            'trackConfig': json.dumps(track_config),
        }

        response = self.post('updateTrackForOrganism', data, autoconvert_to_json=False)
        return response

    def delete_track(self, organism_id, track_label):
        """
        Remove a track from an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type track_label: str
        :param track_label: Track label

        :rtype: dict
        :return: a dictionary with information about the deleted track
        """
        data = {
            'organism': organism_id,
            'trackLabel': track_label,
        }

        response = self.post('deleteTrackFromOrganism', data)
        return response
