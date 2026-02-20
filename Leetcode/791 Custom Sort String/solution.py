from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        result = []

        # Add characters in the order given
        for ch in order:
            if ch in counter:
                result.append(ch * counter[ch])
                del counter[ch]  # remove it so we don't add again

        # Add remaining characters not in order
        for ch, count in counter.items():
            result.append(ch * count)

        return "".join(result)