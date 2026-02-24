class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c ** 0.5)

        while low <= high:
            cur = low * low + high * high

            if cur == c:
                return True
            elif cur > c:
                high -= 1
            else:
                low += 1

        return False
