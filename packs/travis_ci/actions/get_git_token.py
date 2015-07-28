from lib.action import TravisCI
import yaml
import requests


class GetGitToken(TravisCI):
    def run(self):
        username = self.config['username']
        password = self.config['password']
        url = 'https://api.github.com/authorizations'
        host = 'api.github.com'
        ContentType = 'application/json'
        data = '{"scopes": ["read:org", "user:email",\
                "repo_deployment","repo:status", "write:repo_hook"],\
                "note": "toke for travis api"}'
        headers = {}
        headers['Host'] = host
        headers['Content-Type'] = ContentType
        response = requests.post(url, data=data, auth=(username, password),
                                 headers=headers)
        res = yaml.load(response.content)
        self.config['token'] = res['token']
