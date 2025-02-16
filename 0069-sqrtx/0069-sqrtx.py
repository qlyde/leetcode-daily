class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x // 2
        while l <= r:
            m = (l + r) // 2
            sq = m * m
            if sq < x:
                l = m + 1
            elif sq > x:
                r = m - 1
            else:
                return m
        return r
        