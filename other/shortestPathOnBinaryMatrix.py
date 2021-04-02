from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1]):
            return -1
        
        q = deque()
        q.append(((0,0),1))
        grid[0][0] = 1
        
        moves = [(0,1),(1,1),(1,0),(0,-1),(-1,1),(1,-1),(-1,-1),(-1,0)]
        
        while(q):
            curr , currDistance = q.popleft()
            
            if(curr[0] == len(grid) - 1 and curr[1] == len(grid) - 1):
                return currDistance
                
            for move in moves:
                dest_i, dest_j = move[0] + curr[0], move[1] + curr[1] 
                if(0<= dest_i <len(grid) and 0<= dest_j <len(grid[0]) and grid[dest_i][dest_j] == 0):
                    grid[dest_i][dest_j] = 1
                    q.append(((dest_i,dest_j), currDistance + 1))
                    
        return -1
        
