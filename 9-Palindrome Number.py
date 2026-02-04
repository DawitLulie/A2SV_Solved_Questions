class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = str(x)
        return result == result[::-1]