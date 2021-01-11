class Solution:
    def art_sum(self,num):
        return (num -1)*(num)//2
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        comp = dict()
        for i in nums:
            try:
                if comp[i] == 0:
                    comp[i] = 1
                else:
                     comp[i] += 1
            except:
                comp[i] = 1
                
        print(comp)
        count = 0
        for key in comp.keys():
            if(comp[key] > 1):
                count += self.art_sum(comp[key])
            
        return count
    
