class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        arr = s.split()
        set_ = set()
        if len(arr) != len(pattern):
            return False

        for i in range(len(arr)):
            if arr[i] in dic and dic[arr[i]] != pattern[i]:
                return False

            elif arr[i] not in dic and  pattern[i] in set_:
                return False

            dic[arr[i]] = pattern[i]
            set_.add(pattern[i])

        return True
        