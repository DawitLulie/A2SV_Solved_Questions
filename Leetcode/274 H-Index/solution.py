class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        n = len(citations)
        h_index = 0

        for i in range(n):
            if citations[i] >= i + 1:
               h_index =  i + 1

        
        return h_index
        
        