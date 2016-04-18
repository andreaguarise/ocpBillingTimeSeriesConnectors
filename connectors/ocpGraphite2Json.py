import sys
import Config
import MetricFile
import Metrics
import Tenants
import RESTClient
import re

#class OutputFile:
#    def __init__(self):    

class JsonTransform:
    def __init__(self,json,config):
        self.json =json
        self.config = config
        
    def tenantTransform(self,metric):
        #print "Transform Use key:" + metric
        #print "Will tansform target:" + self.json[0]['target']
        regexp = "(.*)." + metric
        p = re.compile(regexp)
        m = p.findall(self.json[0]["target"]) #"m[0] shall contain the tenant string"
        newMetric = metric #Also metric should be translated using a translation table
        if self.config.has_option("MetricTranslations",metric):
                newMetric = self.config.get("MetricTranslations",metric)
                #print "matching:" + metric + " --> " + newMetric
        if m: 
            if self.config.has_option("TenantTranslations",m[0]):
                newTenant = self.config.get("TenantTranslations",m[0])
                #print "matching:" + m[0] + " --> " + newTenant
                self.json[0]["target"] = newTenant + "." + newMetric
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
for gMetric in graphite.metrics: 
    print JsonTransform(graphite.get(gMetric,""),conf).tenantTransform(gMetric[0])

