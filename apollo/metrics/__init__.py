"""
Contains possible interactions with the Apollo Metrics
"""
from apollo.client import Client


class MetricsClient(Client):
    CLIENT_BASE = '/metrics/'

    def get_metrics(self):
        """
        Get all server metrics

        :rtype: dict
        :return: A dictionary with all of the server timing / metrics
        """
        return self.get('metrics', {})
