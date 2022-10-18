class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyHashSet:
    
    def __init__(self):
        self.head = Node(-1)
    
    def add(self, key: int) -> None:
        if not self.head.next:
            self.head.next = Node(key)
            return self.head.next
        
        curr = self.head.next
        prev = self.head
        while curr:
            if curr.val == key:
                return curr
            prev = curr
            curr = curr.next
        
        prev.next = Node(key)
        return prev.next
    
    def remove(self, key: int) -> None:
        if not self.head.next:
            return False
        
        curr = self.head
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return True
            curr = curr.next
        
        return False
    
    def contains(self, key: int) -> bool:
        curr = self.head.next
        
        while curr:
            if curr.val == key:
                return curr
            curr = curr.next
        return None

