class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        res = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                c = 1
                while num + 1 in s:
                    c += 1
                    num += 1
                res = max(res, c)
        return res
