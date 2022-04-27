class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # conceph: bfs, mark visit point
        row, col = len(grid), len(grid[0])
        
        visit = set()
        islands = 0
        
        def bfs(x, y):
            q = collections.deque()
            q.append((x, y))
            visit.add((x, y))       
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while q:
                px, py = q.popleft()
                for dx, dy in directions:
                    nx, ny = px+dx, py+dy
                    if ((nx in range(row)) and 
                        (ny in range(col)) and
                        grid[nx][ny] == "1" and
                        (nx, ny) not in visit):
                            q.append((nx, ny))
                            visit.add((nx, ny))
                            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    islands += 1
        
        return islands
