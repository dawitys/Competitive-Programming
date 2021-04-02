class Solution:
    def trailingZeroes(self,n: int) -> int:
        cnt = 0
        while n != 0:
            n = n // 5
            cnt = cnt + n  # NOT incremented by 1. Incremented by n.
        return cnt
