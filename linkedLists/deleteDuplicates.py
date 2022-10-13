class ListNode:
    
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    
    def deleteDuplicates(self, head):
        
        temp = head
        
        while temp and temp.next:
            while temp.val == temp.next.val:
                temp.next = temp.next.next
                if temp.next is None:
                    break
                    
            temp = temp.next
        
        return head