class Solution:
    # O(n log n) without stack
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        fleet = 0

        prev_t = -1
        for p, t in cars:
            if t > prev_t:
                fleet += 1
                prev_t = t


        return fleet
