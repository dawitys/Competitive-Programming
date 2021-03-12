# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        totalSum = 0
        def traverse(node,offset1,offset2):
            nonlocal totalSum
            if not node: return
            
            if offset2:
                totalSum += node.val
            
            offset2 = offset1
            offset1 = (node.val%2 == 0)
            
            traverse(node.left,offset1,offset2)
            traverse(node.right,offset1,offset2)
        
        traverse(root,False,False)
        return totalSum
