import Config
import MetricFile
import Metrics
import Tenants
import Graphite
import sys


        

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()


metricFile = MetricFile.MetricFile(conf.get("Producer","outFile"))
print "Reading metrics from file:" + metricFile.name
metricListOut = Metrics.Metrics()
while metricFile.readline():
    metricListOut.append(metricFile.getMetric(metricFile.lastline))
    Graphite.Graphite(conf.get("Graphite","Url")).postMetric(metricFile.getMetric(metricFile.lastline))
#metricListOut.output()
    