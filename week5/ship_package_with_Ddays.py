class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while(left < right):
            mid = (left + right )// 2 
            
            if(self.possibleCapacity(mid,weights) < D):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def possibleCapacity(self,amount,weights):
        count, total = 0, 0
        for i in weights:
            if (total + i) > amount:
                total = i
                count += 1
            else:
                total += i
        return count
            
