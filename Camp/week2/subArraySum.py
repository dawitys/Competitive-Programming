class Solution:
    def subarraySum(self,nums, k):
        runningSum = {0:1}
        total = 0
        run = 0
        for i in range(len(nums)):
            run += nums[i]
            total += runningSum.get(run-k,0)
            
            runningSum[run] = runningSum.get(run,0) + 1
            
        return total
