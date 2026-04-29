class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[y].append(x)

        def dfs(index, visited, nums):
            
            for nei in graph[index]:
                if not visited[nei]:
                    visited[index] = True
                    nums.add(nei)
                    dfs(nei, visited, nums)
            
            return nums
            
        result = []
        for i in range(n):
           visited = [False] * n
           nums = dfs(i, visited, set())    
           result.append(sorted(nums))
        
        return result


        
        


        