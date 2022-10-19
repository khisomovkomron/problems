class Queue:
    
    def __int__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        self.queue[0]
    
    def queue_size(self):
        pass
    
    def is_empty(self):
        return self.queue == []
    