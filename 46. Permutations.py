class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(l):
            if l == len(nums):
                res.append(nums.copy())
            
            for i in range(l, len(nums)):
                nums[i], nums[l] = nums[l], nums[i]
                backtrack(l + 1)
                nums[i], nums[l] = nums[l], nums[i]

        backtrack(0)
        return res
