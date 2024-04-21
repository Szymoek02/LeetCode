# TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        cache = {}
        def bruteforce(i):
            nonlocal res
            if i == len(s):
                res += 1
                return
            if s[i] == '0':
                return


            bruteforce(i + 1)
            if (i + 1) < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                bruteforce(i + 2)
        
        bruteforce(0)
        return res

# Time: O(n) Space: O(n) 
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            digit1 = int(s[i - 1])
            digit2 = int(s[i - 2: i])

            if 1 <= digit1 <= 9:
                dp[i] += dp[i - 1]

            if 10 <= digit2 <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

# Full dynamic programming - constans space
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        a = b = 1

        for i in range(2, n + 1):
            digit1 = int(s[i - 1])
            digit2 = int(s[i - 2: i])
            res = 0
            if 1 <= digit1 <= 9:
                res += b

            if 10 <= digit2 <= 26:
                res += a

            a = b
            b = res

        return b
            

            

        
            

            

        
