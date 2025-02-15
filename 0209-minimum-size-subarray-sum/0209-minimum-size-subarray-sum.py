class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        windowSum = 0
        l = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            while l < r and windowSum - nums[l] >= target:
                windowSum -= nums[l]
                l += 1
            if windowSum >= target:
                res = min(res, r - l + 1)
        return res if res != float("inf") else 0
