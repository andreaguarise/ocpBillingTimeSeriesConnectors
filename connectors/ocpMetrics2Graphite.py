import Config
import MetricFile
import Metrics
import Tenants
import Graphite


conf = Config.Config('./test.conf')
conf.read()

print "Now reading..."
metricFile = MetricFile.MetricFile(conf.get("Producer","outFile"))
metricListOut = Metrics.Metrics()
while metricFile.readline():
    metricListOut.append(metricFile.getMetric(metricFile.lastline))
    Graphite.Graphite(conf.get("Graphite","Url")).postMetric(metricFile.getMetric(metricFile.lastline))
#metricListOut.output()
    