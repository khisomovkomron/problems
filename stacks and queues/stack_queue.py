class Queue:
    
    def __int__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    def enqueue(self, data):
        self.enqueue_stack.append(data)
    
    def dequeue(self):
        
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception('Stacks are empty')
        
        if len(self.dequeue_stack) == 0:
            
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        
        return self.dequeue_stack.pop()

if __name__ == '__main__':
    
    en = Queue()
    
    en.enqueue(5)
    en.enqueue(10)
    en.enqueue(20)
    
    