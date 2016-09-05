import datetime
import RESTClient
import os

class Graphite:
    def __init__(self,url):
        self.host,self.port = url.split(":")
    
    def postMetric(self,metric):
        dt = datetime.datetime.strptime(metric.time,"%d-%m-%Y %H:%M:%S")
        command = ('echo "ocp.ceilometer.tenant.' + 
            metric.host.tenant.replace(" ", "_") + '.' + 
            'host.' + metric.host.name.replace(" ", "_") +
            '.' + str(metric.name) +
            ' ' +
            str(int(round(float(metric.value)))) + ' ' + str(dt.strftime("%s")) + '" | nc ' + str(self.host) + ' ' +str(self.port))
        print command    
        os.system(command)
        
class GraphiteRender:
    def __init__(self,config):
        self.baseUri = config.get("Graphite","RenderUri")
        self.metrics = config.items("GraphiteMetrics")
        self.renderFrom = config.get("Graphite","RenderFrom")
        
    def get(self,metric,constraints):
        uri = self.baseUri + "/render?target=" + metric[1] + "&" + "from=" + self.renderFrom + "&format=json"
        print uri
        rest = RESTClient.RESTClient(uri)
        rest.get()
        return rest.json_body_load()