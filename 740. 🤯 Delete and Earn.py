class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_lookup = [0] * (max(nums) + 1)
        
        for n in nums:
            num_lookup[n] += n

        dp = [0] * len(num_lookup)
        dp[1] = num_lookup[1] 
        
        for n in range(2, len(num_lookup)):
            dp[n] = max(num_lookup[n] + dp[n - 2], dp[n - 1])
        return dp[-1]
