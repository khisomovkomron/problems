class Node:
    
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    
    dummy = Node(-1)
    dummy.next = head
    
    actual_node = dummy
    
    while actual_node.next:
        if actual_node.next.val == val:
            actual_node.next = actual_node.next.next
        else:
            actual_node = actual_node.next
            
    return actual_node.next