class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # concept: each union from different system eliminate a single island point
        length = len(grid)
        width = len(grid[0])
        islands = length*width
        gs = list(range(length*width))
        
        def find(x):
            while x != gs[x]: x = gs[x]
            return x
  
        def union(x, y, islands):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                gs[rooty] = rootx
                islands -= 1
            return islands

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # union all grids
        for i in range(length):
            for j in range(width):
                if grid[i][j] == "0": # sea node 
                    islands -= 1
                    continue
                curpos = i*width+j
                for dx, dy in directions: # four neighbors
                    nx, ny = i+dx, j+dy
                    if (nx in range(length) and ny in range(width) and
                        grid[nx][ny] == "1"):
                        grid[i][j] = "0"
                        npos = nx*width+ny
                        islands = union(curpos, npos, islands)
                        #print("gs islands", gs, islands)
                
        return islands
                
