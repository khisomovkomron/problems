from dataclasses import dataclass

@dataclass
class Queue1:

    stack = []
        
    def enqueue(self, data):
        self.stack.append(data)
        
    def dequeue(self):

        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()

        self.stack.append(item)

        return dequeued_item
    

stack = Queue1()

stack.enqueue(5)
stack.enqueue(10)
stack.enqueue(15)
stack.enqueue(20)
print(stack.dequeue())