class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # O(k * len(s))
        while len(s) > k:
            r = ""
            for i in range(0, len(s), k):
                r += str(sum([int(c) for c in s[i:i+k]]))
            s = r
        return s
