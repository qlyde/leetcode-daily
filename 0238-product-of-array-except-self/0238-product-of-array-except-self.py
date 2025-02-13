class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1) excluding output arr mem
        res = [*nums]
        for i in range(len(nums)):
            nums[i] = nums[i] * (nums[i - 1] if i != 0 else 1)

        suff = 1
        for i in range(len(res) - 1, -1, -1):
            temp = (nums[i - 1] if i != 0 else 1) * suff
            suff *= res[i]
            res[i] = temp

        return res
