import json

import requests 


class RESTClient:
    def __init__(self, uri):
        self.uri = uri
 
    def get(self):
        r = requests.get(self.uri)
        self.status_code = r.status_code
        self.headers = r.headers
        self.body = r.text
    
    def json_body_load(self):
        return json.loads(self.body)
    