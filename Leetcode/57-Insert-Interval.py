class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval] 
            
        result = []
        start, end = newInterval[0], newInterval[1]
        inserted = False

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0] or intervals[i][0] > newInterval[1]:
                if not inserted and intervals[i][0] > newInterval[1]:
                    inserted = True
                    result.append([start, end])

                result.append(intervals[i])

            else:
                if intervals[i][0] < start:
                    start = intervals[i][0]

                if intervals[i][1] > end:
                    end = intervals[i][1]
                    
        if not inserted:
            result.append([start, end])

        return result


