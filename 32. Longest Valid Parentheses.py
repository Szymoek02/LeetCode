class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ok = [0] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    ok[i] = 1
                    ok[stack.pop()] = 1

        count = 0
        ans = 0
        for i in ok:
            if i:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans
