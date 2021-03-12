# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None

        new_val=max(nums)
        split_index=nums.index(new_val)
        node=TreeNode(new_val)
        if len(nums[:split_index]):
            node.left=self.constructMaximumBinaryTree(nums[:split_index])
        if len(nums[split_index+1:]):
            node.right=self.constructMaximumBinaryTree(nums[split_index+1:])

        return node
