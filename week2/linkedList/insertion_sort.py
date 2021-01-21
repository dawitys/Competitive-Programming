# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        # if head is empty or only have 1 element, return head
        if not head: return None
        if not head.next: return head
        
        dummy = ListNode(None,head)
        current = head
        
        while current.next is not None:
            if current.next.val >= current.val:
                current = current.next
                
            else: 
                temp = current.next
                runner = dummy
                current.next = current.next.next

                while runner.next.val <= temp.val:
                    runner = runner.next
                runner.next, temp.next = temp, runner.next
                
        return dummy.next   
        