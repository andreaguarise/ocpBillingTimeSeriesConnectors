import sys
import Config
import Metrics
import Tenants

confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()
pillarBaseUri = conf.get("Pillar","baseUri")
metrics = conf.items("Metrics")
print "Reading tenant list from: " + pillarBaseUri
tenants = Tenants.Tenants(pillarBaseUri)
metricList = Metrics.Metrics()
for tenant in tenants.get():
    hosts = tenant.getHosts()
    if hosts != None:
        for host in hosts.list:
                host.get()
                for metric in metrics:
                    metricBuffer = host.getMetric(conf,metric[0])
                    metricList.append(metricBuffer)
outputFile = conf.get("Producer","outFile")
print "Writing metrics in output file:" + outputFile
metricList.output(outputFile)

