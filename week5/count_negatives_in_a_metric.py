class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        count = 0
        
        j = 0
        i = n - 1
        while(i >= 0 and j < m):
            if grid[i][j] < 0:
                count += m-j
                i -= 1
            else:
                j += 1
        return count
            
        
                