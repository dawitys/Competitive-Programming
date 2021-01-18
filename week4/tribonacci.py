class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t0 = 0
        t1 = 1
        t2 = 1
        
        if n == 0:
            return t0
        
        for i in range(n - 2):
            temp = t2 + t1 + t0
            temp2 = t1
            t1 = t2
            t0 = temp2
            t2 = temp
            
        return t2