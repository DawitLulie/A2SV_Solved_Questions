class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = min(strs, key = len)
        min_len = len(small) 
        for word in strs:
            for i in range(min_len):
                if word[i] != small[i]:
                    min_len = i
                    break

        return small[:min_len]