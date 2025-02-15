class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        expected = 1
        for num in nums:
            if num == expected:
                expected += 1

        return expected
        