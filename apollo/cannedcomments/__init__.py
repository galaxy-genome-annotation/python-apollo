"""
Contains possible interactions with the Apollo Canned Comments Module
"""
from apollo.client import Client


class CannedCommentsClient(Client):
    CLIENT_BASE = '/cannedComment/'

    def add_comment(self, comment, metadata=""):
        """
        Add a canned comment

        :type comment: str
        :param comment: New canned comment

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: A dictionnary containing canned comment description
        """
        data = {
            'comment': comment,
            'metadata': metadata
        }

        return self.post('createComment', data)

    def get_comments(self):
        """
        Get all canned comments available in this Apollo instance

        :rtype: list of dicts
        :return: list of canned comment info dictionaries
        """
        return self.post('showComment', {})

    def show_comment(self, value):
        """
        Get a specific canned comment

        :type value: str
        :param value: Canned comment to show

        :rtype: dict
        :return: A dictionnary containing canned comment description
        """
        comments = self.get_comments()
        comments = [x for x in comments if x['comment'] == value]
        if len(comments) == 0:
            raise Exception("Unknown comment")
        else:
            return comments[0]

    def update_comment(self, id_number, new_value, metadata=None):
        """
        Update a canned comment

        :type id_number: int
        :param id_number: canned comment ID number

        :type new_value: str
        :param new_value: New canned comment value

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number,
            'new_comment': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateComment', data)

    def delete_comment(self, id_number):
        """
        Update a canned comment

        :type id_number: int
        :param id_number: canned comment ID number

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number
        }

        return self.post('deleteComment', data)
