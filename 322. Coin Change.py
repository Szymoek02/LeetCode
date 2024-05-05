# Top-down memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(n):
            if n == 0: return 0
            if n in cache: return cache[n]

            res = math.inf
            for c in coins:
                if c <= n:
                    res = min(res, dfs(n - c) + 1)
            cache[n] = res
            return res

        res = dfs(amount)
        return res if res != math.inf else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[-1] if dp[-1] != math.inf else -1
