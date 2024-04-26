class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][1:]) + grid[i][j]
                elif j == (n - 1):
                    dp[i][j] = min(dp[i-1][:j]) + grid[i][j]
                else:
                    dp[i][j] = min(min(dp[i-1][:j]), min(dp[i-1][j+1:])) + grid[i][j]
        return min(dp[n - 1])
