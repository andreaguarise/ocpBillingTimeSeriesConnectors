class Metric:
    def __init__(self,host,name,time,value):
        self.host = host
        self.name = name
        self.time = time
        self.value = value

class Metrics: 
    def __init__(self):
        self.list = []
        
    def append(self,metric):
        self.list.append(metric)
        
    def output(self,out = ""):
        if out != "":
            outfile = open(out, 'w')
            for m in self.list:
                print >> outfile, m.host.tenant + ";" + m.host.name + ";" + str(m.name)    + ";" +  str(m.time) + ";" + str(m.value)
        else:
            for m in self.list:
                print m.host.tenant + ";" + m.host.name + ";" + str(m.name)    + ";" +  str(m.time) + ";" + str(m.value)