class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "]":
                cur = ""
                while stack and  stack[-1] != "[":
                       cur = stack.pop() + cur
                num = ""

                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(cur * int(num))

            else:
                stack.append(ch)

        return "".join(stack)






        