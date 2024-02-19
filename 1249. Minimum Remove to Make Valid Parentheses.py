class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ok = [0] * len(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    ok[stack.pop()] = 1
                    ok[i] = 1

        ans = ""
        for i, c in enumerate(s):
            if c in "()":
                if ok[i]:
                    ans += c
            else:
                ans += c

        return ans

            