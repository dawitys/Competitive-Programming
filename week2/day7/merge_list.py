# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        res = ListNode()
        tail = res
        while(p1 is not None and p2 is not None):
            if(p1.val < p2.val):
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        while(p1 is not None):
            tail.next = p1
            p1 = p1.next
            tail = tail.next
                
        while(p2 is not None):
            tail.next = p2
            p2 = p2.next  
            tail = tail.next
        return res.next