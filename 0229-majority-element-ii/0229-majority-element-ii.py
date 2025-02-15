class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        res = []
        for elem, cnt in c.items():
            if cnt > len(nums) // 3:
                res.append(elem)
        return res
