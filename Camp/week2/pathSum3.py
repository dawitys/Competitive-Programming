# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sums = [0]
        running = 0
        dp = defaultdict(int)
        self.recurse(root,dp,running,sums,sum)
        return sums[0]
        
    def recurse(self, node, dp, running, sums, sum):
        if node == None:
            return 
        running += node.val
        if running == sum:
            sums[0]+= 1
        if running-sum in dp:
            sums[0] += dp[running-sum] 

        dp[running]+= 1
        self.recurse(node.left,dp, running, sums, sum)
        self.recurse(node.right,dp, running, sums, sum)
        dp[running]-= 1
