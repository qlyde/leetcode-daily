class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time: O(n)
        # Space: O(1)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            if nums[i] != val:
                i += 1
        return i
