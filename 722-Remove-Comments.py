class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        arr = []
        comment = False

        for word in source:
            i = 0
            while i < len(word):
                if not comment and i < len(word) - 1 and word[i : i + 2] == "//":
                    break

                if not comment and i < len(word) - 1 and word[i : i + 2] == "/*":
                    comment = True
                    i += 2
                    continue

                if comment and i < len(word) - 1 and word[i : i + 2] == "*/":
                    comment = False
                    i += 2
                    continue

                if not comment:
                    arr.append(word[i])

                i += 1

            if not comment:
                line = "".join(arr)
                if line:
                    result.append("".join(arr))
                arr = []

        return result
