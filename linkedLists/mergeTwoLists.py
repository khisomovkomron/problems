class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) -> list:
        newHead = dummyHead = ListNode()
        
        while list1 and list2:
            if list1.val < list2:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
            
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
            
        return newHead.next
    
if __name__ == '__main__':
    
    linkedLists = Solution()
    linkedLists.mergeTwoLists(list1=[1,2,4], list2 = [1,3,4])