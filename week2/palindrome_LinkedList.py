class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        while fast is not None and fast.next is not None:
            tmp = slow

            slow = slow.next
            fast = fast.next.next

            tmp.next = reversed_list
            reversed_list = tmp

        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None:
            if(reversed_list.val != slow.val):
                return False
            reversed_list = reversed_list.next
            if(slow == None):
                return False
            slow = slow.next

        return True