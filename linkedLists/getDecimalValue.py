def getdecimalbinary(head):
    
    answer = 0
    
    while head:
        answer = 2*answer + head.val
        head = head.next
    return answer