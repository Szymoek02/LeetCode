class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            if t <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res 
#???
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            t = sum([math.ceil(pile / k) for pile in piles])
            if t <= h:
                res = min(res, k)
                l = k - 1
            else:
                r = k + 1
        return res
#???
