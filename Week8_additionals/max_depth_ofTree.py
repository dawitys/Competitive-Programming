"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 1
        s = []
        s.append(root)
        while (s):
            curr = s.pop()
            count += 1
            if(curr.children):
                s.append(curr.children.pop())
        return count
        
