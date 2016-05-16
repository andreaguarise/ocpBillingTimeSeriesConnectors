import sys
import Config
import File
import Metrics
import Tenants
from Graphite import GraphiteRender
from JsonTransform import JsonTransform

        
confFile = "./test.conf"
if len(sys.argv) > 1:
    confFile = sys.argv[1]
conf = Config.Config(confFile)
conf.read()

graphite = GraphiteRender(conf)
print "reading metrics from: " + graphite.baseUri
outputList = []
for gMetric in graphite.metrics: 
    metric = graphite.get(gMetric,"")
    outputList.append((gMetric[0],JsonTransform(metric,conf).map(gMetric[0])))#Refator this. It's just unreadable

outputPath = "/tmp/"
if conf.has_option("ocpGraphite2Jason","path"):
            outputPath = conf.get("ocpGraphite2Jason","path")    
file = File.OutputFile(outputPath,outputList)
file.write()

