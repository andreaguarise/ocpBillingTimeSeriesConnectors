class Message:
    def __init__(self,content):
        self.content = content
    def produce(self): pass
    def consume(self): pass
    def __repr__(self):
        return "Message content: " + self.content
    
if __name__ == '__main__':
    msg = Message("Sample\nmessage\ncontent\n")
    print msg
    
    
