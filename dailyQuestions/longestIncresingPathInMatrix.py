class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1 for i in range(len(matrix[j]))] for j in range(len(matrix))]
        moves = [(0,-1),(-1,0),(1,0),(0,1)]
        
        def dfs(pos):
            if(dp[pos[0]][pos[1]] == -1):
                max_move = 1
                for move in moves:
                    dest_i, dest_j = pos[0] + move[0] , pos[1] + move[1]
                    if( (0 <= dest_i < len(matrix)) and (0 <= dest_j < len(matrix[0])) and (matrix[pos[0]][pos[1]] < matrix[dest_i][dest_j])):
                        c = dfs((dest_i,dest_j))
                        max_move = max(max_move, c + 1)
                dp[pos[0]][pos[1]] = max_move
                return max_move
            else:
                return dp[pos[0]][pos[1]]
                
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] == -1:
                    dp[i][j] = dfs((i,j))
                    
        return max([max(dp[j]) for j in range(len(dp))])
        
