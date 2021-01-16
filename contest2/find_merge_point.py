# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    p1 = head1
    p2 = head2
    while not None:
        if p1 == p2:
            break
        p1 = p1.next
        p2= p2.next
        # Begin again if one was shorter than the other
        if p1 == None:
            p1 = head1
        if p2 == None:
            p2 = head2
    return p1.data