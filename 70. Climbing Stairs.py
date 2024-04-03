# backtracing recursive tree
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.dp(memo, n)

    def dp(self, memo, n):
        if n == 1 or n == 0:
            return 1

        if n not in memo:
            memo[n] = self.dp(memo, n - 1) + self.dp(memo, n - 2)

        return memo[n]

# tabulation - skip

# full dp approach - bottom up
# base case -> solution 
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        
        for i in range(n):
            temp = b
            b = a + b
            a = temp

        return b
