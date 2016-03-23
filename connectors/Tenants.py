import Hosts
import RESTClient


class Tenant:
    def __init__(self,name,uri):
        self.name = name
        self.uri = uri + name.replace(" ", "%20")
        
    def get(self):
        rest = RESTClient.RESTClient(self.uri)
        rest.get()
        return rest
    
    def getHosts(self):
        rest = RESTClient.RESTClient(self.uri + "/hosts")
        rest.get()
        buff = rest.json_body_load()["result"]["groups"]
        try:
            result = []
            for h in buff[0]["paasMachines"]:
                result.append(h["machineName"]) 
        except:
            return None
        else:    
            return Hosts.Hosts(result,self.name,self.uri)

class Tenants:
    def __init__(self,pillarBaseUri):
        self.uri = pillarBaseUri + 'groups/'
    
    def get(self):
        rest = RESTClient.RESTClient(self.uri)
        rest.get()
        tenants = []
        tdict =  rest.json_body_load()['result']['groups']
        for t in tdict:
            tenants.append(Tenant(t['groupName'],self.uri))
        return tenants