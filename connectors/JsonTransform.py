import re

class JsonTransform:
    def __init__(self,json,config):
        self.json = json
        self.config = config
        
    def map(self,metric):
        print "Transform Use key:" + metric       
        regexp = "(.*)." + metric
        p = re.compile(regexp)
        for element in self.json:
            print "Will tansform target:" + element['target']
            m = p.findall(element["target"]) #"m[0] shall contain the tenant string"
            newMetric = metric #Also metric should be translated using a translation table
            if self.config.has_option("MetricTranslations",metric):
                    newMetric = self.config.get("MetricTranslations",metric)
                    print "matching:" + metric + " --> " + newMetric
                    if m: 
                        if self.config.has_option("TenantTranslations",m[0]):
                            newTenant = self.config.get("TenantTranslations",m[0])
                            print "matching:" + m[0] + " --> " + newTenant
                            element["target"] = newTenant + "." + newMetric               
        return self.json