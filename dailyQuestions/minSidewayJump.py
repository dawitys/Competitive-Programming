class Solution:
    def minSideJumps(self, A):
        dp = [1, 0, 1]
        for a in A:
            if a:
                dp[a - 1] = float('inf')
            for i in xrange(3):
                if a != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
