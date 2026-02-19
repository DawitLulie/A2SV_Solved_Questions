class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        result = 1
        cur = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > cur:
                result += 1
                cur = points[i][1]

            if points[i][1] < cur:
                cur = points[i][1]

        return result
        