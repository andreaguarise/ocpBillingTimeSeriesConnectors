import Config
import MetricFile
import Metrics
import Tenants
import Graphite


confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()

print "Now reading..."
metricFile = MetricFile.MetricFile(conf.get("Producer","outFile"))
metricListOut = Metrics.Metrics()
while metricFile.readline():
    metricListOut.append(metricFile.getMetric(metricFile.lastline))
    Graphite.Graphite(conf.get("Graphite","Url")).postMetric(metricFile.getMetric(metricFile.lastline))
#metricListOut.output()
    