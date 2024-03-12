class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        window, need = {}, {}
        for i in t:
            need[i] = 1 + need.get(i, 0)
        l = 0
        countT, countS = 0, len(need)
        res = [-1, -1]
        resLen = float("infinity")
        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in need.keys() and window[c] == need[c]:
                countT += 1
            while countT == countS:
                if resLen > (r - l + 1):
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in need.keys() and window[s[l]] < need[s[l]]:
                    countT -= 1
                l += 1
        l, r = res
        return s[l:r + 1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        window, need = {}, {}
        for i in t:
            need[i] = 1 + need.get(i, 0)
        l = 0
        countT, countS = 0, len(need)
        res = ""
        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in need.keys() and window[c] == need[c]:
                countT += 1
            while countT == countS:
                if len(res) > len(s[l:r + 1]) or res == "":
                    res = s[l:r + 1]
                window[s[l]] -= 1
                if s[l] in need.keys() and window[s[l]] < need[s[l]]:
                    countT -= 1
                l += 1
        return res
