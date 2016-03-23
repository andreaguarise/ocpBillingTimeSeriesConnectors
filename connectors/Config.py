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