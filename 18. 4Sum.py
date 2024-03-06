class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def isDistinct(a, b, c, d):
            return a != b and a != c and a != d \
            and b != c and b != d and d != c

        hm = {} # value : index
        res = set()
        n = len(nums)
        for i in range(n):
            hm[nums[i]] = i

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x = target - nums[i] - nums[j] - nums[k]
                    if x in hm and isDistinct(i, j, k, hm[x]):
                        ans = tuple(sorted([nums[i], nums[j], nums[k], x]))
                        res.add(ans)

        return res
