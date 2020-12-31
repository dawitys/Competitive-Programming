class Solution:
    def reverse(self, x: int) -> int:
        isPosetive = True
        if x<0:
            isPosetive = False
            x=abs(x)
        num_str = str(x)
        if(isPosetive):
           res = int(num_str[::-1]) 
        else:
            res = 0 - int(num_str[::-1]) 
        return res