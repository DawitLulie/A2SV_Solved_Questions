class Solution:
    def pow(x, n, mod):
        if n == 0:
            return 1
        half = pow(x, n // 2, mod)
        if n % 2 == 0:
            return (half * half) %  mod

        return (half * half * x ) % mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n+1) // 2
        odd = n // 2
        
        return (pow(5, even, mod) * pow(4,odd,mod)) % mod
       