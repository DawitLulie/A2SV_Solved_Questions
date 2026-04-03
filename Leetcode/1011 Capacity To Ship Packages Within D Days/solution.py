class Solution:
    def shipWithinDays(self, weights: List[int], days: int):
        def check(num):
            cur_sum = 0
            day = 1   
            
            for weight in weights:
                cur_sum += weight
                
                if cur_sum > num:
                    day += 1
                    cur_sum = weight

            return day <= days   



        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1   

        return left