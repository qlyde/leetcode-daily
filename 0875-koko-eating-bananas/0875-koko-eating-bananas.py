class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile / speed)
            return hours

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            hours = getHours(m)
            if hours > h:
                l = m + 1
            elif hours <= h:
                r = m
        return l

