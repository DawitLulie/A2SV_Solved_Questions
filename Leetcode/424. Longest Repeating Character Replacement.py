class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = Counter()
        max_len = 0
        left = 0
        result = 0

        for right in range(len(s)):
            ch = s[right]
            dic[ch] += 1
            
            max_len = max(max_len, dic[ch])

            while (right - left + 1) - max_len > k:
                dic[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
