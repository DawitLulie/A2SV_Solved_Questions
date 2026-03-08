class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)

        for first, last, seats in bookings:
            diff[first] += seats
            diff[last + 1] -= seats

        for i in range(1, n + 1):
            diff[i] += diff[i-1]

        return diff[1:n+1]