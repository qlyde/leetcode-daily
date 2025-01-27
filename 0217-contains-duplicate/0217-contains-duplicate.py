class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(n)
        return len(nums) > len(set(nums))
