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
