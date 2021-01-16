# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    nodes = []
    current_node = head
    while(current_node != None):
        if current_node in nodes:
            return 1
        nodes.append(current_node)
        current_node = current_node.next
    return 0
        