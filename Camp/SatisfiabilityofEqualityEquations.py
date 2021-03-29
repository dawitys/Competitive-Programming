class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [[i,0] for i in range(26)]
        
        
        def f(e):
            if e == leader[e][0]:
                return e
            leader[e][0] = f(leader[e][0])
            return leader[e][0]
        
        def union(a,b):
            if(leader[a][1]> leader[b][1]):
                a,b = b,a
                
            #Rank by num of nodes    
            leader[a][1] += leader[b][1]
            leader[b][1] += leader[a][1]
            
            a_parent = f(a)
            b_parent = f(b)
            
            leader[a_parent][0] = b_parent
            
        for eqn in equations:            
            if(eqn[1] == "="):
               union(f(ord(eqn[0]) - ord('a')),f(ord(eqn[-1]) - ord('a')))
            
        for eqn in equations:
            if eqn[1] == "!" and f(ord(eqn[0]) - ord('a')) == f(ord(eqn[-1]) - ord('a')): 
               return False 
        return True
