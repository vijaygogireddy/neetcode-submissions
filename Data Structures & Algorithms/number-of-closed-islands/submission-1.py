import sys
sys.setrecursionlimit(2000000)

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in [0, cols-1]:
                dfs(r,c)

        for c in range(cols):
            for r in [0, rows-1]:
                dfs(r,c)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r,c)


        return count
