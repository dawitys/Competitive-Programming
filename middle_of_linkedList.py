class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,first):
        self.first = first

def findMedian(linkedList):
    slow = linkedList.first
    fast = linkedList.first

    while(slow.next != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    return slow

node5 = Node("Node5",None)
node4 = Node("Node4",node5)
node3 = Node("Node3",node4)
node2 = Node("Node2",node3)
node1 = Node("Node1",node2)

ll= LinkedList(node1)
mid = findMedian(ll)
print(mid.data)