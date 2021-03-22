class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        a = sorted(A)
        
        for i in range(len(a)):
            if(K and a[i] < 0):
                a[i] = -1 * a[i]
                K -= 1
            else:
                if(K % 2 == 0):
                    break
                else:
                    if( a[i] < a[i-1]):
                        a[i] = -1 * a[i]
                    else:
                        a[i-1] = -1 * a[i-1]
                    break
                    
            
        return sum(a)
