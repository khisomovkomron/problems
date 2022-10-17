def isPalindrome(head) -> bool:
    
    
    # First method
    ls = []
    
    while head:
        ls.append(head.val)
        head = head.next
        
    if ls == ls[::-1]:
        return True
    else:
        return False
    

def isPalindrome2(head) -> bool:
    
    def reverse(prev, head):
        if not head:
            return prev
        tmp = head.next
        head.next = prev
        return reverse(head, tmp)
    
    sp = head
    fp = sp
    
    while fp and fp.next():
        sp = sp.next
        fp = fp.next.next
        
        
    mid = reverse(None, sp)
    
    def check(mid, head):
        if not mid:
            return True
        elif mid.val == head.val:
            return check(mid.next, head.next)
        else:
            return False
    
    return check(mid, head)