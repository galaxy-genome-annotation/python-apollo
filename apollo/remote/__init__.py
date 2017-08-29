"""
Contains possible interactions with the Apollo Organisms Module
"""
from apollo.client import Client


class RemoteClient(Client):
    CLIENT_BASE = '/organism/'

    def add_organism(self, common_name, organism_data, blatdb=None, genus=None,
                     species=None, public=None, non_default_translation_table=None, metadata=None):
        """
        Add an organism using the remote organism API

        :type species: str
        :param species: Species

        :type genus: str
        :param genus: Genus

        :type blatdb: str
        :param blatdb: Server-side Blat directory for the organism

        :type public: bool
        :param public: should the organism be public

        :type common_name: str
        :param common_name: Organism common name

        :type non_default_translation_table: int
        :param non_default_translation_table: The translation table number for
                                              the organism (if different than
                                              that of the server's default)

        :type metadata: str
        :param metadata: JSON formatted arbitrary metadata

        :type organism_data: file
        :param organism_data: .tar.gz or .zip archive containing the data directory.

        :rtype: dict
        :return: a dictionary with information about the new organism
        """
        data = {
            'commonName': common_name,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        response = self.post('addOrganismWithSequence', list(data.items()), files={'organismData': organism_data}, autoconvert_to_json=False)

        return [x for x in response if x['commonName'] == common_name]
