class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split("/")
        stack = []

        for word in words:
            if word == "..":
               if stack:
                 stack.pop()

            elif word != "" and word != ".":
                stack.append(word)
                
        return "/" + "/".join(stack)

        