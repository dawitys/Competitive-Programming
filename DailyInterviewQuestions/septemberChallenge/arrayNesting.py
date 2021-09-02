class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def dfs(i,elts):
            while(nums[i] not in elts):
                elts.add(nums[i])
                dfs(nums[i],elts)

            
        maxNestingLength = 0
        for i in range(len(nums)):
            elements = set()
            dfs(i,elements)
            length = len(elements)
            maxNestingLength = max(maxNestingLength,length)
            
        return maxNestingLength
