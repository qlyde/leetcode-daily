class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        for l in range(len(height)):
            maxL[l] = max(height[l], maxL[l - 1]) if l != 0 else height[l]
        for r in range(len(height) - 1, -1, -1):
            maxR[r] = max(height[r], maxR[r + 1]) if r != len(height) - 1 else height[r]
        res = 0
        for i in range(len(height)):
            res += max(0, min(maxL[i], maxR[i]) - height[i])
        return res
        