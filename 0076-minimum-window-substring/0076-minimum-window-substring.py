class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = (0, float("inf"))
        wFreqs = defaultdict(int)
        tFreqs = defaultdict(int)
        for ch in t:
            tFreqs[ch] += 1

        have, need = 0, len(tFreqs)
        l = 0
        for r in range(len(s)):
            wFreqs[s[r]] += 1
            if wFreqs[s[r]] == tFreqs[s[r]]:
                have += 1

            while l < r and wFreqs[s[l]] > tFreqs[s[l]]:
                wFreqs[s[l]] -= 1
                if wFreqs[s[l]] < tFreqs[s[l]]:
                    have -= 1
                l += 1
                
            if have == need and r - l < res[1] - res[0]:
                res = (l, r)
        return s[res[0]:res[1] + 1] if res != (0, float("inf")) else ""
        