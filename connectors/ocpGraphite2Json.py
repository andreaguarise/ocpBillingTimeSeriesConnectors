import sys
import Config
import MetricFile
import Metrics
import Tenants

class GraphiteRender:
    def __init__(self,config):
        self.baseUri = conf.get("Graphite","RenderUri")
        self.metrics = conf.items("GraphiteMetrics")
        self.renderFrom = conf.get("Graphite","RenderFrom")
        
    def get(self,metric,constraints):
        uri = self.baseUri + "/render?target=" + metric[1] + "&" + "from=" + self.renderFrom + "&format=json"
        print uri

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()
graphite = GraphiteRender(conf)
print "reading metrics from: " + graphite.baseUri
for gMetric in graphite.metrics: print graphite.get(gMetric,"format=json&from=-10days")

