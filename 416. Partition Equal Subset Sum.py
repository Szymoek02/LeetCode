class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
                
        # def dfs(target, i):
        #     if i >= len(nums) or target < 0: return False
        #     if target == t: return True

        #     return dfs(target + nums[i], i + 1) or dfs(target, i + 1)

        # return dfs(0, 0)

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                if t + nums[i] == s // 2 : return True
                nextDP.add(t + nums[i])
            dp = nextDP
        return s // 2 in dp
0,5,11,10,16,6,12,17
[1,5,11,5]
