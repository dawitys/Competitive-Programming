class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = dict()
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[i])-1,-1,-1):
                if(i == len(grid)-1 and j == len(grid[i]) - 1):
                    dp[(i,j)] = grid[i][j]
                elif(j == len(grid[i])-1):
                    dp[(i,j)] = grid[i][j] + dp[(i+1,j)]
                elif(i == len(grid) - 1):
                    dp[(i,j)] = grid[i][j] + dp[(i,j+1)]
                else:
                    dp[(i,j)] = grid[i][j] + min(dp[(i+1,j)],dp[(i,j+1)])
                    
                
        return dp[(0,0)]
