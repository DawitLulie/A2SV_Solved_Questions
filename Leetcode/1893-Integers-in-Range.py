class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        arr = [num for num in range(left, right+1)]
        i = j = 0
        while i < len(arr) and j < len(ranges):
            if ranges[j][0] <= arr[i] <= ranges[j][1]:
                i += 1
            else:
                j += 1
        return i == len(arr)

        