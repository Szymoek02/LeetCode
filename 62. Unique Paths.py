class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        grid = [[-1 for _ in range (n)] for _ in range(m)]
        def dfs(r, c):
            if grid[r][c] != -1:
                return grid[r][c]

            if r == 0 and c == 0:
                return 1

            left, down = 0, 0
            if r > 0: 
                left = dfs(r - 1, c)
            if c > 0: 
                down = dfs(r, c - 1)

            grid[r][c] = left + down
            return grid[r][c] 

        dfs(m - 1, n - 1)
        return grid[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        grid = [[0 for _ in range (n)] for _ in range(m)]

        for c in range(n):
            grid[0][c] = 1
        
        for r in range(m):
            grid[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r][c - 1] + grid[r - 1][c]

        return grid[-1][-1]

            
