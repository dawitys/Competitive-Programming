class Solution(object):
    def minDeletionSize(self, A):

        ret = 0
        
        for c in zip(*A): 
            if list(c) != sorted(c): 
                ret += 1
                
        return ret 
