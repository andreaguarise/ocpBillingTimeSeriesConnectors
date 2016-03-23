import datetime
import os

class Graphite:
    def __init__(self,url):
        self.host,self.port = url.split(":")
    
    def postMetric(self,metric):
        dt = datetime.datetime.strptime(metric.time,"%d-%m-%Y %H:%M:%S")
        command = ('echo "ocp.ceilometer.tenant.' + 
            metric.host.tenant.replace(" ", "_") + '.' + 
            'host.' + metric.host.name.replace(" ", "_") +
            '.' + str(metric.name) +
            ' ' +
            str(int(round(float(metric.value)))) + ' ' + str(dt.strftime("%s")) + '" | nc faust01.to.infn.it 2003')
        print command    
        os.system(command)