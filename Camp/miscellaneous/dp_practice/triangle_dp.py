class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = dict()
        
        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])-1,-1,-1):
                if(i == len(triangle)-1):
                    dp[(i,j)] = triangle[i][j]
                else:
                    dp[(i,j)] = triangle[i][j] + min(dp[(i+1,j)],dp[(i+1,j+1)])
                    #del dp[(i+1,j)]
                    #del dp[(i+1,j+1)]
        
        return dp[(0,0)]
