class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        for k in reversed(range(len(key))):
            grid = [math.inf] * len(ring)
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dst = min(abs(r - i), len(ring) - abs(r - i))
                        grid[r] = min(grid[r], min_dst + 1 + dp[i])

            dp = grid
        return dp[0]


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}

        def helper(r, k):
            if k == len(key): return 0
            if (r, k) in cache: return cache[(r, k)]
            res = math.inf

            for i, c in enumerate(ring):
                if c == key[k]:
                    min_dst = min(abs(r - i), len(ring) - abs(r - i))
                    res = min(res, min_dst + 1 + helper(i, k + 1))
            cache[(r, k)] = res
            return res

        return helper(0, 0)
