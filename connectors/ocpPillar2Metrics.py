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
outputFile = conf.get("Producer","outFile")
print "Will write metrics in output channel:" + outputFile
metricList = Metrics.MetricsFile()#FIXME: Use appropriate class File or Stomp on the basis of the protocol specified in conf file. 
tenants = Tenants.Tenants(pillarBaseUri)#Get tenant list from the monitoring Pillar
for tenant in tenants.get():#Get tenant list from monitoring pillare REST interface
    print "\nTENANT NAME:" + tenant.name
    hosts = tenant.getHosts()# For each Tenant in the list get the hosts (VM) used by that tenant
    for host in hosts.list:# For each host get the JSON with the last information available
        print "****HOST NAME:" + host.name
        for metric in metrics:#For each metric defined in the conf file get the metric from the REST interface and append the metric in a list
            print "*****SEARCH FOR METRIC: "+ metric[0]
            metricBuffer = host.getMetric(conf,metric[0])
            metricList.append(metricBuffer)
metricList.output(outputFile)# write metrics down in output file

#output file format:
#Virtual machines;zabbix-agent;iaascpu;09-05-2016 11:22:36;587373.44
#Virtual machines;zabbix-agent;iaascpuutil;09-05-2016 11:22:37;100.0008
#Virtual machines;zabbix-agent;iaasmemory;09-05-2016 11:22:16;4.0
#Virtual machines;zabbix-agent;iaasvcpus;09-05-2016 11:22:18;2.0

