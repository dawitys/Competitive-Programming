class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = [0]
        visited = set()

        def dfs(city):
            visited.add(city)
            found_neighbour = False
            for j in range(1,len(isConnected)+1):
                if(isConnected[city-1][j-1] == 1 and j not in visited):
                    found_neighbour = True
                    dfs(j)
            if(not found_neighbour):
                count[0] +=1
                return
             
        for i in range(len(isConnected)):
            if(i+1 not in visited):
                dfs(i +1)
            
        return count[0]

#         N = len(A)
#         seen = set()
#         def dfs(node):
#             for nei, adj in enumerate(A[node]):
#                 if adj and nei not in seen:
#                     seen.add(nei)
#                     dfs(nei)
#         ans = 0
#         for i in xrange(N):
#             if i not in seen:
#                 dfs(i)
#                 ans += 1
#         return an
