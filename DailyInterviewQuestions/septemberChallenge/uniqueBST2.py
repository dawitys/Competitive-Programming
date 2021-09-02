
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        result = []
        for i in range(start, end+1):
            left = self.dfs(start, i-1)
            right = self.dfs(i+1, end)
            for l in left:
                for r in right:
                    temp = TreeNode(i)
                    temp.left = l
                    temp.right = r
                    result.append(temp)
        return result
