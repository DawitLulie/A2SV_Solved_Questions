class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        num = min(a, b)
        return sum(1 for i in range(1, num + 1) if a  % i == 0 and b % i == 0)

        