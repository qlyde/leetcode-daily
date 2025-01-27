class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        m = {}
        for i in range(len(nums)):
            if (n := target - nums[i]) in m:
                return [m[n], i]
            m[nums[i]] = i
