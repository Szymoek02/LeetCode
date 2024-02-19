class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxRight = maxLeft = 0
        res = 0
        while l < r:
            water = 0
            if height[l] < height[r]:
                water = maxLeft - height[l]
                maxLeft = max(height[l], maxLeft)
                l += 1
            else:
                water = maxRight - height[r]
                maxRight = max(height[r], maxRight)
                r -= 1
            if water > 0:
                res += water 
        return res

        