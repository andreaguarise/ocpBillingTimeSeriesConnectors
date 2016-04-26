import sys
import Config
import MetricFile
import Metrics
import Tenants
import RESTClient
import re
import json

class OutputFile:
    def __init__(self,config,list):
        self.list = list
        if config.has_option("ocpGraphite2Jason","path"):
            self.path = config.get("ocpGraphite2Jason","path")  
        else:
            self.path = "/tmp/"            
        
    def write(self):
        for l in self.list:
            fileName = self.path + "/" + l[0] + ".json"
            print "file:" + fileName + " content:" 
            print l[1]
            output = open(fileName, 'w')
            content = json.dumps(l[1])
            output.write(content)
            output.close()

class JsonTransform:
    def __init__(self,json,config):
        self.json =json
        self.config = config
        
    def map(self,metric):
        print "Transform Use key:" + metric
        
        regexp = "(.*)." + metric
        p = re.compile(regexp)
        for element in self.json:
            print "Will tansform target:" + element['target']
            m = p.findall(element["target"]) #"m[0] shall contain the tenant string"
            newMetric = metric #Also metric should be translated using a translation table
            if self.config.has_option("MetricTranslations",metric):
                    newMetric = self.config.get("MetricTranslations",metric)
                    #print "matching:" + metric + " --> " + newMetric
                    if m: 
                        if self.config.has_option("TenantTranslations",m[0]):
                            newTenant = self.config.get("TenantTranslations",m[0])
                            #print "matching:" + m[0] + " --> " + newTenant
                            element["target"] = newTenant + "." + newMetric
                
        return self.json

class GraphiteRender:
    def __init__(self,config):
        self.baseUri = conf.get("Graphite","RenderUri")
        self.metrics = conf.items("GraphiteMetrics")
        self.renderFrom = conf.get("Graphite","RenderFrom")
        
    def get(self,metric,constraints):
        uri = self.baseUri + "/render?target=" + metric[1] + "&" + "from=" + self.renderFrom + "&format=json"
        print uri
        rest = RESTClient.RESTClient(uri)
        rest.get()
        return rest.json_body_load()
        

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()
graphite = GraphiteRender(conf)
print "reading metrics from: " + graphite.baseUri
outputList = []
for gMetric in graphite.metrics: 
    outputList.append((gMetric[0],JsonTransform(graphite.get(gMetric,""),conf).map(gMetric[0])))
    
file = OutputFile(conf,outputList)
file.write()

