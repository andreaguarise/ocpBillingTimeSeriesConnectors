import Config
import File
import Tenants
from Graphite import Graphite
import sys


        

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()
#Read a metric file in the format produced by ocpPillar2Metrics and POST it to graphite. 
metricFile = File.MetricFile(conf.get("Producer","outFile"))
graphiteUrl = conf.get("Graphite","Url")
print "Reading metrics from file:" + metricFile.name
while metricFile.readline():
    Graphite(graphiteUrl).postMetric(metricFile.getMetric(metricFile.lastline))
    