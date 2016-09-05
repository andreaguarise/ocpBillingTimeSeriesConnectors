import json
import requests 


class RESTClient:
    def __init__(self, uri):
        self.uri = uri
 
    def get(self):
        print "++++++++REST CALL URI:" + self.uri
        r = requests.get(self.uri)
        self.status_code = r.status_code
        self.headers = r.headers
        self.body = r.text
    
    def json_body_load(self):
        return json.loads(self.body)


#test code    
if __name__ == '__main__':    
    rest = RESTClient('http://192.168.56.101:8082/monitoring/adapters/zabbix/types/service/groups')
    rest.get()
    print rest.body
    print rest.status_code
    print rest.headers
    print "JSON output:"
    print rest.json_body_load()
    tenants = rest.json_body_load()
    print tenants['result']['groups']