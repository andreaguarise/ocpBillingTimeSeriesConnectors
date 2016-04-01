import sys
import Config
import MetricFile
import Metrics
import Tenants

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()
pillarBaseUri = conf.get("Pillar","baseUri")
metrics = conf.items("Metrics")
print "reading tenant list from: " + pillarBaseUri
tenants = Tenants.Tenants(pillarBaseUri)
metricList = Metrics.Metrics()
for t in tenants.get():
    hosts = t.getHosts()
    if hosts != None:
        for h in hosts.list:
                h.get()
                for m in metrics:
                    metric = h.getMetric(conf,m[0])
                    metricList.append(metric)
metricList.output(conf.get("Producer","outFile"))

