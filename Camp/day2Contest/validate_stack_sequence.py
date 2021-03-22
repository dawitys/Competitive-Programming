class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        count = 0
        
        for i in pushed:
            s.append(i)
            while s and s[-1] == popped[count]:
                count += 1
                s.pop()
                
        return count == len(popped)
