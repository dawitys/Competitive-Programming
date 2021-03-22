from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        moves = [
                    ([1,0],[1,0]),
                    ([0,1],[0,1]),
                    ([0,0],[-1,1]),
                    ([0,0],[1,-1])
                ]
        
        q = deque()
        visited = set()
        
        q.appendleft((((0,0),(0,1)),0))
        visited.add(((0,0),(0,1)))
        
        while(q):
            curr = q.pop()
            if(curr[0] == ((len(grid)-1,len(grid)-2),(len(grid)-1,len(grid)-1))):
                return curr[1]
            
            for move in moves:
                dest = ((curr[0][0][0] + move[0][0], curr[0][0][1] + move[0][1]),( curr[0][1][0] + move[1][0], curr[0][1][1] + move[1][1]))
                
                if self.isValid(grid,dest,visited) and self.checkRotate(grid,dest,move):
                    q.appendleft((dest,curr[1]+1))
                    visited.add(dest)
                    
        return -1
        
    def isValid(self,grid,dest,visited):        
        return(
            0 <= dest[0][0] < len(grid) and
            0 <= dest[0][1] < len(grid) and
            0 <= dest[1][0] < len(grid) and
            0 <= dest[1][1] < len(grid) and
            grid[dest[0][0]][dest[0][1]] == 0  and
            grid[dest[1][0]][dest[1][1]] == 0 and
            ((dest[0],dest[1]) not in visited) 
        )
    
    def checkRotate(self, grid, dest, move):
        if move == ([0,0],[-1,1]): #counterclockwise
            return dest[1][0] == dest[0][0] and grid[dest[1][0] + 1][dest[1][1]] == 0
        elif move == ([0,0],[1,-1]): #clockwise 
            return dest[1][1] == dest[0][1] and grid[dest[1][0]][dest[1][1] + 1] == 0
        else:
            return True
