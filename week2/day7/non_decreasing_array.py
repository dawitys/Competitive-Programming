class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                modified = True
        return True