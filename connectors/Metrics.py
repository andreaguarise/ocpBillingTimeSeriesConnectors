class Metric:
    def __init__(self,host,name,time,value):
        self.host = host
        self.name = name
        self.time = time
        self.value = value

class Metrics: 
    def __init__(self):
        self.list = []
    
    def __repr__(self):
        buff = ""
        for m in self.list:
                buff += m.host.tenant + ";" + m.host.name + ";" + str(m.name)    + ";" +  str(m.time) + ";" + str(m.value) + "\n"
        
    def append(self,metric):
        self.list.append(metric)
        
    def output(self):
        print self
  
  
class MetricsFile (Metrics):
      
    def output(self,out):
            outfile = open(out, 'w')
            for m in self.list:
                print >> outfile, m.host.tenant + ";" + m.host.name + ";" + str(m.name)    + ";" +  str(m.time) + ";" + str(m.value)
                
class MetricsStomp (Metrics):
    def __init__(self):
        assert False, "Implement It!"