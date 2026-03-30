class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for s in parts:
            if s == "" or s == ".":
                continue
            elif s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)       