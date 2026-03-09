class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        index = -1
        val = float("inf")
        
        for i in range(len(capacity)):
            if itemSize <= capacity[i] < val:
              val = capacity[i]
              index = i

        return  index 
        