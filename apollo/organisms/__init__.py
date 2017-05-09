"""
Contains possible interactions with the Apollo Organisms Module
"""
from apollo.client import Client


class OrganismsClient(Client):
    CLIENT_BASE = '/organism/'

    def addOrganism(self, commonName, directory, blatdb=None, species=None,
                    genus=None, public=False):
        data = {
            'commonName': commonName,
            'directory': directory,
            'publicMode': public,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        return self.post('addOrganism', data)

    def findAllOrganisms(self):
        return self.post('findAllOrganisms', {})

    def findOrganismByCn(self, cn):
        orgs = self.findAllOrganisms()
        orgs = [x for x in orgs if x['commonName'] == cn]
        if len(orgs) == 0:
            raise Exception("Unknown common name")
        else:
            return orgs[0]

    def findOrganismById(self, id_number):
        orgs = self.findAllOrganisms()
        orgs = [x for x in orgs if str(x['id']) == str(id_number)]
        if len(orgs) == 0:
            raise Exception("Unknown ID")
        else:
            return orgs[0]

    def deleteOrganism(self, organismId):
        return self.post('deleteOrganism', {'id': organismId})

    def deleteOrganismFeatures(self, organismId):
        return self.post('deleteOrganismFeatures', {'id': organismId})

    def getSequencesForOrganism(self, commonName):
        return self.post('getSequencesForOrganism', {'organism': commonName})

    def updateOrganismInfo(self, organismId, commonName, directory, blatdb=None, species=None, genus=None, public=False):
        data = {
            'id': organismId,
            'name': commonName,
            'directory': directory,
            'publicMode': public,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        return self.post('updateOrganismInfo', data)
