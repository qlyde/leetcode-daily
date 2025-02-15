class Solution:
    def isValid(self, s: str) -> bool:
        m = {"}": "{", "]": "[", ")": "("}
        stack = []
        for b in s:
            if b in m:
                if len(stack) == 0 or stack[-1] != m[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        return len(stack) == 0
