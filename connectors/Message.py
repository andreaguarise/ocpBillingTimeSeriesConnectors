class Message:
    def __init__(self,content,destination):
        self.content = content
        self.destination = destination
    def produce(self): pass #subclass must implement
    def consume(self): pass #subclass must implement
    def __repr__(self):
        return "Message destination: " + self.destination + "\nMessage content: " + self.content
    
if __name__ == '__main__':
    msg = Message("Sample\nmessage\ncontent\n","protocol://destination")
    print msg
    
    
