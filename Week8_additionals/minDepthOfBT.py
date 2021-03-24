# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        nodes = []
        nodes.append(root)
        level = 1
        
        while(len(nodes) != 0):
            siz = len(nodes)
            
            for i in range(siz):
                cur = nodes.pop(0)

                if(self.isLeaf(cur)):
                    return level

                if(cur.left):
                    nodes.append(cur.left)
                if(cur.right):
                    nodes.append(cur.right)
                
            level +=1

        return level
    
    def isLeaf(self, node):
        return node.left is None and node.right is None
