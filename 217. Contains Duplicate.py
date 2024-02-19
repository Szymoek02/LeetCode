class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        #s = set(nums)
        #if len(nums) == len(s):
        #    return False
        #else:
        #    return True

        return False