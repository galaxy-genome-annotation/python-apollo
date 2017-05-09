"""
Contains possible interactions with the Apollo's Annotations
"""
from apollo.client import Client
import collections


class AnnotationsClient(Client):
    CLIENT_BASE = '/annotationEditor/'

    def _update_data(self, data):
        if not hasattr(self, '_extra_data'):
            raise Exception("Please call setSequence first")

        data.update(self._extra_data)
        return data

    def setSequence(self, sequence, organism):
        self._extra_data = {
            'sequence': sequence,
            'organism': organism,
        }

    def setDescription(self, featureDescriptions):
        data = {
            'features': featureDescriptions,
        }
        data = self._update_data(data)
        return self.post('setDescription', data)

    def setName(self, uniquename, name):
        # TODO
        data = {
            'features': [
                {
                    'uniquename': uniquename,
                    'name': name,
                }
            ],
        }
        data = self._update_data(data)
        return self.post('setName', data)

    def setNames(self, features):
        # TODO
        data = {
            'features': features,
        }
        data = self._update_data(data)
        return self.post('setName', data)

    def setStatus(self, statuses):
        # TODO
        data = {
            'features': statuses,
        }
        data = self._update_data(data)
        return self.post('setStatus', data)

    def setSymbol(self, symbols):
        data = {
            'features': symbols,
        }
        data.update(self._extra_data)
        return self.post('setSymbol', data)

    def getComments(self, feature_id):
        data = {
            'features': [{'uniquename': feature_id}],
        }
        data = self._update_data(data)
        return self.post('getComments', data)

    def addComments(self, feature_id, comments):
        # TODO: This is probably not great and will delete comments, if I had to guess...
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'comments': comments
                }
            ],
        }
        data = self._update_data(data)
        return self.post('addComments', data)

    def addAttributes(self, feature_id, attributes):
        nrps = []
        for (key, values) in attributes.items():
            for value in values:
                nrps.append({
                    'tag': key,
                    'value': value
                })

        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': nrps
                }
            ]
        }
        data = self._update_data(data)
        return self.post('addAttribute', data)

    def deleteAttribute(self, feature_id, key, value):
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': [
                        {'tag': key, 'value': value}
                    ]
                }
            ]
        }
        data = self._update_data(data)
        return self.post('addAttribute', data)

    def getFeatures(self):
        data = self._update_data({})
        return self.post('getFeatures', data)

    def getSequence(self, uniquename):
        data = {
            'features': [
                {'uniquename': uniquename}
            ]
        }
        data = self._update_data(data)
        return self.post('getSequence', data)

    def addFeature(self, feature, trustme=False):
        if not trustme:
            raise NotImplementedError("Waiting on better docs from project. If you know what you are doing, pass trustme=True to this function.")

        data = {
            'features': feature,
        }
        data = self._update_data(data)
        return self.post('addFeature', data)

    def addTranscript(self, transcript, trustme=False):
        if not trustme:
            raise NotImplementedError("Waiting on better docs from project. If you know what you are doing, pass trustme=True to this function.")

        data = {}
        data.update(transcript)
        data = self._update_data(data)
        return self.post('addTranscript', data)

    # addExon, add/delete/updateComments, addTranscript skipped due to docs

    def duplicateTranscript(self, transcriptId):
        data = {
            'features': [{'uniquename': transcriptId}]
        }

        data = self._update_data(data)
        return self.post('duplicateTranscript', data)

    def setTranslationStart(self, uniquename, start):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmin': start
                }
            }]
        }
        data = self._update_data(data)
        return self.post('setTranslationStart', data)

    def setTranslationEnd(self, uniquename, end):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmax': end
                }
            }]
        }
        data = self._update_data(data)
        return self.post('setTranslationEnd', data)

    def setLongestOrf(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.post('setLongestOrf', data)

    def setBoundaries(self, uniquename, start, end):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmin': start,
                    'fmax': end,
                }
            }]
        }
        data = self._update_data(data)
        return self.post('setBoundaries', data)

    def getSequenceAlterations(self):
        data = {
        }
        data = self._update_data(data)
        return self.post('getSequenceAlterations', data)

    def setReadthroughStopCodon(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.post('setReadthroughStopCodon', data)

    def deleteSequenceAlteration(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.post('deleteSequenceAlteration', data)

    def flipStrand(self, uniquenames):
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.post('flipStrand', data)

    def mergeExons(self, exonA, exonB):
        data = {
            'features': [
                {'uniquename': exonA},
                {'uniquename': exonB},
            ]
        }
        data = self._update_data(data)
        return self.post('mergeExons', data)

    # def splitExon(): pass

    def deleteFeatures(self, uniquenames):
        assert isinstance(uniquenames, collections.Iterable)
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.post('deleteFeature', data)

    # def deleteExon(): pass

    # def makeIntron(self, uniquename, ): pass

    def getSequenceSearchTools(self):
        return self.get('getSequenceSearchTools', {})

    def getCannedComments(self):
        return self.get('getCannedComments', {})

    def searchSequence(self, searchTool, sequence, database):
        data = {
            'key': searchTool,
            'residues': sequence,
            'database_id': database,
        }
        return self.post('searchSequences', data)

    def getGff3(self, uniquenames):
        assert isinstance(uniquenames, collections.Iterable)
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.post('getGff3', data, isJson=False)
