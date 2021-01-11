class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                if(count > max_count):
                    max_count = count
                count -= 1
        return max_count
            
