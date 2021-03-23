# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        if N % 2 == 0:
            return []
        memo = {1:[TreeNode(0)]}
        self.getTree(N, memo)
        return memo[N]
    
    def getTree(self, n, memo):
        
        if n <= 0:
            return []
        
        if n in memo:
            return memo[n]
        
        for x in range(1, n, 2):
            self.getTree(x, memo)
            self.getTree(n-x-1, memo)
            l = memo[x]
            r = memo[n-x-1]

            for left in l:
                for right in r:
                    node = TreeNode(0)
                    node.left = left 
                    node.right = right 
                    memo.setdefault(n, [])
                    memo[n].append(node)
