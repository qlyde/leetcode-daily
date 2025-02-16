class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(capacity):
            res, currSum = 0, 0
            for w in weights:
                if currSum + w > capacity:
                    res += 1
                    currSum = 0
                currSum += w
            return res + 1
        
        l, r = max(weights), sum(weights)  # O(n)

        # Find least x for which getDays(x) <= days
        # O(nlogm), m = sum(weights)
        while l < r:
            m = (l + r) // 2
            d = getDays(m)
            if d <= days:
                r = m
            else:
                l = m + 1
        return l

