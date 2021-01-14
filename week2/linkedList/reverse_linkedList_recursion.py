# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)
            
    def reverse(self,head):
        if(head.next == None):
            return head
        else:
            temp =  self.reverse(head.next)
            head.next = temp
            return temp
        