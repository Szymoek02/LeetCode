class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l +1: r ]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
            
        return max_str

# TODO: Manacher's algorithm
