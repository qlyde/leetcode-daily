class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        p, q = 0, 0
        while p < len(word1) and q < len(word2):
            if p > q:
                res += word2[q]
                q += 1
            else:
                res += word1[p]
                p += 1
        res += word1[p:]
        res += word2[q:]
        return res        
        