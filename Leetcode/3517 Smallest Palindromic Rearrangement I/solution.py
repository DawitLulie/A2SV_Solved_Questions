class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = n // 2
        answer = ""

        if n % 2 == 0:
            answer = "".join(sorted(s[:mid]))
            return answer + answer[::-1]

        else:
            answer = "".join(sorted(s[:mid]))
            return answer + s[mid] + answer[::-1]


        