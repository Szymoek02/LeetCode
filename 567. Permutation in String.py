class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for i in s1:
            freq[i] = 1 + freq.get(i, 0)
        
        w = len(s1)
        for i in range(len(s2) - w + 1):
            count = freq.copy()
            for j in s2[i:i + w]:
                if j in count.keys():
                    count[j] -= 1
            
            if all(count[j] == 0 for j in count.keys()):
                return True

        return False
