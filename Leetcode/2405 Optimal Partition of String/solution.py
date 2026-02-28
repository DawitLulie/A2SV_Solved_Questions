class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        substrings = 0

        for ch in s:
            if ch in seen:
                substrings += 1
                seen.clear()

            seen.add(ch)

        return substrings + 1

                


        