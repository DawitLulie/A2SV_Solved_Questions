class Solution:
    def eraseOverlapIntervals( intervals):
        if not intervals:
            return 0

        intervals.sort()   # sort by start time

        result = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:   # overlap
                result += 1
                prev_end = min(prev_end, end)  # keep smaller end
            else:
                prev_end = end

        return result