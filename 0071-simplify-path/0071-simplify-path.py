class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split("/")
        for i in p:
            if i == "." or i == "":
                continue
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

