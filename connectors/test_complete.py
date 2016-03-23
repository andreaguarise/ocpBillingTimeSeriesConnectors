import Config
import MetricFile
import Metrics
import Tenants
import Graphite


conf = Config.Config('./test.conf')
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
# This goes in another exe
print "Now reading..."
metricFile = MetricFile.MetricFile(conf.get("Producer","outFile"))
metricListOut = Metrics.Metrics()
while metricFile.readline():
    metricListOut.append(metricFile.getMetric(metricFile.lastline))
    Graphite.Graphite(conf.get("Graphite","Url")).postMetric(metricFile.getMetric(metricFile.lastline))
#metricListOut.output()
    