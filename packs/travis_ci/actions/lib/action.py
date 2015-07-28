import httplib
import json
import requests
import yaml
from st2actions.runners.pythonrunner import Action

API_URL = 'https://api.travis-ci.org'
HEADER_ACCEPT = 'application/vnd.travis-ci.2+json'
HEADER_CONTENT_TYPE = 'application/json'


class TravisCI(Action):
    def __init__(self):
        super(TravisCI, self).__init__(config)
        self.travis_token = self._get_travis_token(self.config['token'])

    def _get_base_headers(self):
        headers = {}
        headers['Content-Type'] = HEADER_CONTENT_TYPE
        headers['Accept'] = HEADER_ACCEPT
        return headers

    def _get_auth_headers(self):
        headers = self._get_base_headers()
        headers['Authorization'] = 'token: "%s"' % (self.travis_token)
        return headers

    def _get_travis_token(self, api_key, path='/auth/github'):
        url = API_URL + path
        headers = self._get_auth_headers()
        data = {"github_token": api_key}
        res = requests.post(url, data=json.dumps(data), headers=headers)
        response = yaml.load(res.content)
        return response['access_token']

    def _perform_request(self, path, method, data=None, requires_auth=False):
        url = API_URL + path

        if method == "GET":
            if requires_auth:
                headers = self._get_auth_headers()
            else:
                headers = {}
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            headers = self._get_auth_headers()
            response = requests.post(url, headers=headers)
        elif method == 'PUT':
            headers = self._get_auth_headers()
            response = requests.put(url, data=data, headers=headers)

        if response.status_code in [httplib.FORBIDDEN, httplib.UNAUTHORIZED]:
            msg = ('Invalid or missing Travis CI auth token.'
                   ' Make sure you have'
                   'specified valid token in the config file')
            raise Exception(msg)

        return response
