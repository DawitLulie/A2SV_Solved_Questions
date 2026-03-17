class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(x, m):
            if m == 0:
                return 1
            half = func(x, m // 2)
            if m % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / func(x, -n)
        return func(x, n)