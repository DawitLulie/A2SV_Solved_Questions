class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            num1 = intervals[i][1]
            num2 = intervals[i+1][0]
            num3 = intervals[i+1][1]
            if num1 >= num2:
                last = num3 if num3 > num1 else num1
                intervals[i] = [intervals[i][0], last]
                intervals.remove(intervals[i+1])
            else:
               i += 1
        return intervals

        