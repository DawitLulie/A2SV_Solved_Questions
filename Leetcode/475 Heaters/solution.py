class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        heaters.sort()
        result = 0

        def raduis(target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] == target:
                    return (mid, mid)
            
                elif heaters[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1
            
            return (left, right)
        
        for house in houses:
            left, right = raduis(house)
            minn = float("inf")

            if left < n:
                minn = min(minn,abs(house - heaters[left]))
            
            if right >= 0:
                minn = min(minn,abs(house - heaters[right]))
            
            result = max(result, minn)
    
        return result




            


        

