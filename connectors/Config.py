import ConfigParser


class Config:
    def __init__(self,fileName):
        self.fileName = fileName
    
    def read(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.fileName)
    
    def get(self,section,key):
        return self.config.get(section,key)
    
    def items(self,section):
        return self.config.items(section)
    
    def has_option(self,section,key):
        return self.config.has_option(section,key)
    

#Test code
if __name__ == '__main__':
    conf = Config('./test.conf')
    conf.read()
    print "Get a value:"
    print conf.get("Pillar","baseUri")
    print "Get an array of item tuples:"
    print conf.items("Metrics")
    print "Test an existent item (True):"
    print conf.has_option("Pillar","baseUri")
    print "Test a non existent item (False):"
    print conf.has_option("Not exists","baseUri")