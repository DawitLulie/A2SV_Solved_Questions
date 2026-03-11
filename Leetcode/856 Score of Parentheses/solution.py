class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = 0

        for ch in s:
            cur = 0
            if ch == ")":
                while stack and stack[-1] != "(":
                    cur += stack.pop()

                stack.pop()
                if cur > 0:
                    stack.append(cur * 2)

                else:
                    stack.append(1)
            else:
                stack.append(ch)
                
        return sum(stack)
                
                


        