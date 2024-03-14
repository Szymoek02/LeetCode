class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # sorted [left...mid]
            if nums[l] <= nums[m]:
                # target is in the sorted half 
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # sorted [mid...right]
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1


        return -1
