import Hosts
import Metrics


class MetricFile:
	def __init__(self,name):
		self.name = name
		self.fd = open(name)
		
	def __next__(self):
		return self.readline
		
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
		