"""
Contains possible interactions with the Apollo Canned Comments Module
"""
from apollo.client import Client


class CannedCommentsClient(Client):
    CLIENT_BASE = '/cannedComment/'

    def addComment(self, comment, metadata=""):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'comment': comment,
            'metadata': metadata
        }

        return self.post('createComment', data)

    def findAllComments(self):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        return self.post('showComment', {})

    def findCommentByValue(self, value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        comments = self.findAllComments()
        comments = [x for x in comments if x['comment'] == value]
        if len(comments) == 0:
            raise Exception("Unknown comment")
        else:
            return comments[0]

    def findCommentById(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        comments = self.findAllComments()
        comments = [x for x in comments if str(x['id']) == str(id_number)]
        if len(comments) == 0:
            raise Exception("Unknown ID")
        else:
            return comments[0]

    def updateComment(self, id_number, new_value, metadata=None):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number,
            'new_comment': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateComment', data)

    def deleteComment(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number
        }

        return self.post('deleteComment', data)
