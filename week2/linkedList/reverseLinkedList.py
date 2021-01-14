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
        node = head
        temp = None
        while(node != None ):
            nxt = node.next
            node.next = temp
            temp = node
            node = nxt

        return temp
            