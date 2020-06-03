"""
Contains possible interactions with the Apollo Organisms Module
"""
import json

from apollo.client import Client
from apollo.decorators import raise_error_decorator


class OrganismsClient(Client):
    CLIENT_BASE = '/organism/'

    @raise_error_decorator
    def add_organism(self, common_name, directory, blatdb=None, genus=None,
                     species=None, public=False, metadata=None):
        """
        Add an organism

        :type common_name: str
        :param common_name: Organism common name

        :type directory: str
        :param directory: Server-side directory

        :type blatdb: str
        :param blatdb: Server-side path to 2bit index of the genome for Blat

        :type genus: str
        :param genus: Genus

        :type species: str
        :param species: Species

        :type public: bool
        :param public: Should the organism be public or not

        :type metadata: str
        :param metadata: JSON formatted arbitrary metadata

        :rtype: dict
        :return: a dictionary with information about the new organism
        """
        data = {
            'commonName': common_name,
            'directory': directory,
            'publicMode': public,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species
        if metadata is not None:
            if isinstance(metadata, dict):
                # Apollo wants a string
                metadata = json.dumps(metadata)
            data['metadata'] = metadata

        response = self.post('addOrganism', data)
        # Apollo decides here that it would be nice to return information about
        # EVERY organism. LMAO.
        if type(response) is not list:
            return response
        return [x for x in response if x['commonName'] == common_name][0]

    def update_organism(self, organism_id, common_name, directory, blatdb=None, species=None, genus=None, public=False,
                        no_reload_sequences=False):
        """
        Update an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type common_name: str
        :param common_name: Organism common name

        :type directory: str
        :param directory: Server-side directory

        :type blatdb: str
        :param blatdb: Server-side Blat directory for the organism

        :type genus: str
        :param genus: Genus

        :type species: str
        :param species: Species

        :type public: bool
        :param public: User's email

        :type no_reload_sequences: bool
        :param no_reload_sequences: Set this if you don't want Apollo to reload genome sequences (no change in genome sequence)

        :rtype: dict
        :return: a dictionary with information about the updated organism
        """
        data = {
            'id': organism_id,
            'name': common_name,
            'directory': directory,
            'publicMode': public,
            'noReloadSequences': no_reload_sequences,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        response = self.post('updateOrganismInfo', data)[0]

        if len(response.keys()) == 0:
            return self.show_organism(organism_id)
        return response

    def get_organisms(self, common_name=None):
        """
        Get all organisms

        :type common_name: str
        :param common_name: Optionally filter on common name

        :rtype: list
        :return: Organism information
        """
        if common_name is None:
            orgs = self.post('findAllOrganisms', data={})
        else:
            orgs = self.post('findAllOrganisms', {'organism': common_name})
        return orgs

    def show_organism(self, common_name):
        """
        Get information about a specific organism.

        :type common_name: str
        :param common_name: Organism Common Name

        :rtype: dict
        :return: a dictionary containing the organism's information
        """
        orgs = self.get_organisms(common_name=common_name)
        if isinstance(orgs, list) and len(orgs) > 0:
            orgs = orgs[0]
        return orgs

    def delete_organism(self, organism_id):
        """
        Delete an organim

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: list
        :return: A list of all remaining organisms
        """
        return self.post('deleteOrganism', {'id': organism_id})

    def delete_features(self, organism_id):
        """
        Remove features of an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: dict
        :return: an empty dictionary
        """
        return self.post('deleteOrganismFeatures', {'organism': organism_id})

    def get_sequences(self, organism_id):
        """
        Get the sequences for an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: list of dict
        :return: The set of sequences associated with an organism
        """
        return self.post('getSequencesForOrganism', {'organism': organism_id})

    def get_organism_creator(self, organism_id):
        """
        Get the creator of an organism

        :type organism_id: str
        :param organism_id: Organism ID Number

        :rtype: dict
        :return: a dictionary containing user information
        """
        return self.post('getOrganismCreator', {'organism': organism_id})

    def update_metadata(self, organism_id, metadata):
        """
        Update the metadata for an existing organism.

        :type organism_id: str
        :param organism_id: Organism ID Number

        :type metadata: str
        :param metadata: Organism metadata. (Recommendation: use a structured format like JSON)

        :rtype: dict
        :return: An empty, useless dictionary
        """
        return self.post('updateOrganismMetadata', {'id': organism_id, 'metadata': metadata})
