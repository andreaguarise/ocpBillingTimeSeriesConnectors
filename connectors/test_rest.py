import RESTClient


rest = RESTClient.RESTClient('http://192.168.56.101:8082/monitoring/adapters/zabbix/types/service/groups')
rest.get()
print rest.body
print rest.status_code
print rest.headers
print "JSON output:"
print rest.json_body_load()
tenants = rest.json_body_load()
print tenants['result']['groups']