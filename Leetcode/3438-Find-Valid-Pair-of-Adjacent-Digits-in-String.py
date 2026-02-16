class Solution:
    def findValidPair(self, s: str) -> str:
        dic = Counter(s)
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if a != b and dic[a] == int(a) and dic[b] == int(b):
                return "".join([s[i], s[i+1]])

        return ""

        