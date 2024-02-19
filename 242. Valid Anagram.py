class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i not in letters.keys():
                letters[i] = 1
            else:
                letters[i] += 1
        
        for i in t:
            if i not in letters.keys():
                return False
            else:
                letters[i] -= 1
        
        for i in letters.keys():
            if letters[i] != 0:
                return False

        return True