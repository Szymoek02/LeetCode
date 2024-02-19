class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        nums1Idx = {v : i for i, v in enumerate(nums1)}
        for i in range(len(nums2)):
            x = nums2[i]
            while len(stack) > 0 and x > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = x
            #we are only interested in numbers in nums2 that are in nums1
            if x in nums1:
                stack.append(x)

        return res
