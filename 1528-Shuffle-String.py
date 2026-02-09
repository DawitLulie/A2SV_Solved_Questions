class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [''] * len(s)
        for i in range(len(s)):
            index = indices[i]
            arr[index] = s[i]
        return "".join(arr)
        
        
