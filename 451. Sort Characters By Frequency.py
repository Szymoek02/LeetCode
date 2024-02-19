class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        for i in s:
            print(i)
            if i not in letters.keys():
                letters[i] = 1
            else:
                letters[i] += 1

        letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
        ans = ""
        for k, v in letters.items():
            ans += k * v
        return ans

        