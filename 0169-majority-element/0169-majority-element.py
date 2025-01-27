class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        m = {}
        for num in nums:
            m[num] = 1 + m.get(num, 0)
            if m[num] >= len(nums) / 2:
                return num
