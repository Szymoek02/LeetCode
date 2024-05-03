# Top down memoization
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= m or c >= n:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
                else:
                    cache[(r, c)] = 0

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

# Dynamic programming bottom up
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        
        for i in range(n):
            dp[0][i] = int(matrix[0][i])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down = dp[i + 1][j])
                right = dp[i][j + 1]
                diag = dp[i + 1][j + 1]
                
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(down, right, diag)

        print(dp)
        return max([max(i) for i in dp]) ** 2
