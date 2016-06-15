from stomp import *
import sys

class Message:
    def __init__(self,content,destination):
        self.content = content
        self.destination = destination
    def connect(self): pass
    def disconnect(self): pass
    def produce(self): pass #subclass must implement
    def consume(self): pass #subclass must implement
    def __repr__(self):
        return "Message destination: " + self.destination + "\nMessage content: " + self.content
 
class Stomp (Message):
    def connect(self,listener=None):
        host,port,self.queue = self.destination.split(':')
        print "Contacting host: " + host + ", port: " + port
        self.conn = Connection([(host,int(port))])
        if listener != None:
            self.conn.set_listener('', PrintingListener())
        self.conn.start()
        self.conn.connect('','',wait=True)#username,password,wait?
    def disconnect(self):
        self.conn.disconnect()
        
    def produce(self):
        print "Produce:" 
        print self.queue
        self.conn.send(self.queue,self.content)
        
    def consume(self):
        self.conn.subscribe(self.queue,123)#queue,#?
        
    
        
                                
if __name__ == '__main__':
    msg = Message("Sample\nmessage\ncontent\n","protocol://destination")
    print msg
    if len(sys.argv) > 1:
        destination = sys.argv[1]
    stmp = Stomp("Sample\nmessage\ncontent\n",destination)
    stmp.connect()
    stmp.produce()
    stmp.disconnect()
    stmp.connect(PrintingListener())
    stmp.consume()
    stmp.disconnect()
    

        