class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = math.inf * -1
        currSum = 0

        for n in nums:
            currSum = max(n, currSum + n)
            bestSum = max(bestSum, currSum)

        return bestSum
