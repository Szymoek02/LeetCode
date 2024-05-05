# Prefix sum solution
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        prefix = [[0 for j in range(C + 1)] for i in range(R + 1)]

        for x in range(R):
            for y in range(C):
                prefix[x + 1][y] = prefix[x][y] + int(matrix[x][y])
                #prefix[x][y] = prefix[x][y - 1] + int(matrix[x][y])

        def all_ones(top, bot, y):
            return (prefix[bot + 1][y] - prefix[top][y]) == (bot - top + 1)
        
        for p in prefix:
            print(p)

        res = 0
        for top in range(R):
            for bot in range(top, R):

                curr = 0
                for y in range(C):
                    if all_ones(top, bot, y):
                        curr += 1
                    else:
                        curr = 0

                    res = max(res, curr * (bot - top + 1))

        return res
        
