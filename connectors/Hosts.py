import Metrics
import RESTClient


class Host:
	def __init__(self,name,tenant,uri):
		self.name = name
		self.tenant =tenant
		self.uri = uri + "/hosts/"  + name.replace(" ", "%20")
		
	def get(self):	
		rest = RESTClient.RESTClient(self.uri)
		rest.get()
		return rest
	
	def getMetric(self,conf,metricName):
		uri = self.uri + conf.get("Metrics",metricName)
		print "GET METRIC " + uri
		rest = RESTClient.RESTClient(uri)
		rest.get()
		if rest.status_code == 200:
			value = rest.json_body_load()["result"]["groups"][0]["paasMachines"][0]["services"][0]["paasMetrics"][0]["metricValue"]
			time = rest.json_body_load()["result"]["groups"][0]["paasMachines"][0]["services"][0]["paasMetrics"][0]["metricTime"]
			metric = Metrics.Metric(self,metricName,time,value)
			return metric
		

class Hosts:
	def __init__(self,hostList,tenant,uri):
		self.list = []
		self.uri = uri
		for h in hostList:
			self.list.append(Host(h,tenant,uri))
	
