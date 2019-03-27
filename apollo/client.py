"""Base apollo client
"""
import json
import logging

import requests
try:
    from shlex import quote
except ImportError:
    from pipes import quote
log = logging.getLogger()


class Client(object):
    """
    Base client class implementing methods to make requests to the server
    """
    CLIENT_BASE = '/'

    def __init__(self, webapolloinstance, **requestArgs):
        self._wa = webapolloinstance

        self.__verify = requestArgs.get('verify', True)
        self._request_args = requestArgs

        if 'verify' in self._request_args:
            del self._request_args['verify']

    def post(self, client_method, data, post_params=None, is_json=True):
        """Make a POST request"""
        url = self._wa.apollo_url + self.CLIENT_BASE + client_method

        if post_params is None:
            post_params = {}

        headers = {
            'Content-Type': 'application/json'
        }

        data.update({
            'username': self._wa.username,
            'password': self._wa.password,
        })

        curl_command = ['curl', url]
        for (k, v) in headers.items():
            curl_command += ['-H', quote('%s: %s' % (k, v))]
        curl_command += ['-d', quote(json.dumps(data))]
        log.info(' '.join(curl_command))

        resp = requests.post(url, data=json.dumps(data),
                             headers=headers, verify=self.__verify,
                             params=post_params, allow_redirects=False,
                             **self._request_args)

        if resp.status_code == 200 or resp.status_code == 302:
            if is_json:
                data = resp.json()
                return self._scrub_data(data)
            else:
                return resp.text

        # @see self.body for HTTP response body
        raise Exception("Unexpected response from apollo %s: %s" %
                        (resp.status_code, resp.text))

    def get(self, client_method, get_params, is_json=True):
        """Make a GET request"""
        url = self._wa.apollo_url + self.CLIENT_BASE + client_method
        headers = {}

        response = requests.get(url, headers=headers,
                                verify=self.__verify, params=get_params,
                                **self._request_args)
        if response.status_code == 200:
            if is_json:
                data = response.json()
                return self._scrub_data(data)
            else:
                return response.text
        # @see self.body for HTTP response body
        raise Exception("Unexpected response from apollo %s: %s" %
                        (response.status_code, response.text))

    @classmethod
    def _scrub_data(cls, data):
        """Remove sensitive attributes from response data"""
        if 'username' in data:
            del data['username']
        if 'password' in data:
            del data['password']
        return data
