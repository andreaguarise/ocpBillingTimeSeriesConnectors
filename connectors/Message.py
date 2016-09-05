from stomp import *
import sys
#Classes to implement communication to JMS messaging system. Used to implement he Message Endpoint (ref. EIP) for each command.
class Message:#FIXME: refactor, better call this Channel
    def __init__(self,destination):
        self.destination = destination
        self.content  = ""
    def connect(self): pass
    def disconnect(self): pass
    def produce(self,content): pass #subclass must implement
    def consume(self): pass #subclass must implement
    def __repr__(self):
        return "Message destination: " + self.destination + "\nMessage content: " + self.content
 
class Stomp (Message):
    def connect(self,listener=None):
        host,port,self.queue = self.destination.split(':')
        print "Contacting host: " + host + ", port: " + port
        self.conn = Connection([(host,int(port))])
        if listener != None:
            self.conn.set_listener('', PrintingListener())#FIXME, get listener class form listener input variable
        self.conn.start()
        self.conn.connect('','',wait=True)#username,password,wait?
    def disconnect(self):
        print "Disconnect."
        self.conn.disconnect()
        
    def produce(self,content):
        print "Produce:" + content 
        print self.queue
        self.content = content
        self.conn.send(self.queue,self.content)
        
    def consume(self):
        print "Consume:"
        self.conn.subscribe(self.queue,123)#queue,#?
        #FIXME implement. Should put each received message in an array. 
        
class File(Message):
    #FIXME file based messages, directory as channel, file as message 
        
                                
if __name__ == '__main__':
    msg = Message("protocol://destination")
    print msg
    if len(sys.argv) > 1:
        destination = sys.argv[1]
    stmp = Stomp(destination)
    stmp.connect()
    stmp.produce("Message 1")
    stmp.produce("Message 2")
    stmp.produce("Message 3")
    stmp.disconnect()
    stmp.connect(PrintingListener())
    stmp.consume()
    stmp.disconnect()
    

        