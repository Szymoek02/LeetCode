class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    if l := (nums[i], nums[left], nums[right]):
                        ans.add(l)    
                        left += 1
                        right -= 1

        return ans