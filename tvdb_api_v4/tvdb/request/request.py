import json
import urllib.parse
import urllib.request
from urllib.request import urlopen


class Request:
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def make_request(self, url):
        req = urllib.request.Request(url)
        req.add_header("Authorization", "Bearer {}".format(self.auth_token))
        with urllib.request.urlopen(req) as response:
            res = json.load(response)
            data = res["data"]
            return data
