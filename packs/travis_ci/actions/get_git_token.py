from lib.action import TravisCI
import json
import requests


class GetGitToken(TravisCI):
    def run(self):
        username = self.config['username']
        password = self.config['password']
        url = 'https://api.github.com/authorizations'
        host = 'api.github.com'
        ContentType = 'application/json'
        data = {"scopes": ["read:org", "user:email",
                "repo_deployment", "repo:status", "write:repo_hook"],
                "note": "token for travis api"}
        headers = {}
        headers['Host'] = host
        headers['Content-Type'] = ContentType
        response = requests.post(url, data=json.dumps(data),
                                 auth=(username, password),
                                 headers=headers)
        res = response.json()
        self.config['token'] = res['token']
