class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        for ch in s1:
            target[ord(ch) - ord("a")] += 1

        window = [0] * 26
        l = 0
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if window == target:
                    return True
                window[ord(s2[l]) - ord("a")] -= 1
                l += 1
        return False
        