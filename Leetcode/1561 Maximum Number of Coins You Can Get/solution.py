class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        left, right  = 0, len(piles)
        result = 0

        while left < right:
            left += 1
            right -= 2
            result += piles[right]
            
        return result


        