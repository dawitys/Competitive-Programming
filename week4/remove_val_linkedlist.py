# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        while(current != None and current.next != None):
            if(current.next.val == val):
                current.next = current.next.next
                continue
            current = current.next
        
        if head != None and head.val == val:
            head = head.next
            
        return head