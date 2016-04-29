import Hosts
import Metrics
import json


class MetricFile:
	def __init__(self,name):
		self.name = name
		self.fd = open(name)
			
	def readline(self):
		self.lastline = self.fd.readline()
		return self.lastline
	
	def getMetric(self,line):	
		(a,b,c,d,e) = line.strip().split(';')
		h = Hosts.Host(b,a,"")
		return Metrics.Metric(h,c,d,e)
		
	def readMetric(self):	
		(a,b,c,d,e) = self.readline().strip().split(';')
		h = Hosts.Host(b,a,"")
		return Metrics.Metric(h,c,d,e)
	
	
class OutputFile:
    def __init__(self,path,filelist):
        self.list = filelist
        self.path = path            
        
    def write(self):
        for l in self.list:
            fileName = self.path + "/" + l[0] + ".json"
            print "file:" + fileName + " content:" 
            print l[1]
            output = open(fileName, 'w')
            content = json.dumps(l[1])
            output.write(content)
            output.close()

#test code    
if __name__ == '__main__':
	file = MetricFile("./test.conf")
	while file.readline():
		print "Line:" + file.lastline	
	
		