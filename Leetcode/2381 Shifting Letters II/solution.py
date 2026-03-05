class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        result = []
        for i in range(n):
            new_char = (ord(s[i]) - 97 + prefix[i]) % 26 + 97
            result.append(chr(new_char))

        return "".join(result)