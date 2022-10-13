class Node:
    
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def getIntersectionNode(self, headA, headB):
        
        dummyA, dummyB = headA, headB
        
        while dummyA != dummyB:
            
            dummyA = headB if dummyA is None else dummyA.next
            dummyB = headA if dummyB is None else dummyB.next
            
        return dummyA