class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(n * m)
        # Space: O(1)
        if len(strs) == 1:
            return strs[0]

        ans = ""
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        
        return ans
