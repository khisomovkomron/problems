class ListNode:
    
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    
    def hasCycle(self, head):
        
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == next:
                return True
        return False