class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(n * m)
        # Space: O(n * m)
        def mapCount(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            return tuple(count)

        ans = {}
        for s in strs:
            count = mapCount(s)
            if count in ans:
                ans[count].append(s)
            else:
                ans[count] = [s]
        return list(ans.values())
