class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(pos, curr, t):
            if t == 0:
                res.append(curr.copy())
                return
            if t < 0 or pos >= len(candidates):
                return
                
            prev = -1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, t - candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res

            
