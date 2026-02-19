class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = Counter()
        dic2 = Counter(t)

        left = 0
        min_len = float("inf")
        start = end = 0  
        formed = 0  
        required = len(dic2)

        for right in range(len(s)):
            if s[right] in dic2:
                dic1[s[right]] += 1
                if dic1[s[right]] == dic2[s[right]]:
                    formed += 1

            while formed == required:
                window = right - left + 1
                if window < min_len:
                    min_len = window
                    start = left
                    end = right

                if s[left] in dic1:
                    if dic1[s[left]] == dic2[s[left]]:
                        formed -= 1
                    dic1[s[left]] -= 1
                    if dic1[s[left]] == 0:
                        del dic1[s[left]]

                left += 1

        return s[start:end + 1] if min_len < float("inf") else ""
