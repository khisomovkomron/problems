class Stack:
    
    def __int__(self):
        self.stack = []
        
    def pop(self):
        if self.stack_size() < 1:
            return -1
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, data):
        self.stack.append(data)
        
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)
    