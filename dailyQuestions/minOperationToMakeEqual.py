class Solution(object):
    def minOperations(self, n):
        #arthematic sum
        #return n*n//4
        count = (n + 1) // 2
        first = n - 1
        last = n - (2 * count - 1)
        return count * (first + last) // 2
