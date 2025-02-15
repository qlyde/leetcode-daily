class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freqs = defaultdict(int)
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            maxFreq = max(maxFreq, freqs[s[r]])
            if r - l + 1 - maxFreq > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res