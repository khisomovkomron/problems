def middleNode(head):
    
    slow = head
    fast = head
    
    while fast and fast.head:
        
        slow = slow.next
        fast = fast.next.next
        
    return slow