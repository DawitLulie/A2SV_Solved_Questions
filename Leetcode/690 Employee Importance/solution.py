class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        n = max(employees, key=lambda x: x.id).id
        val = [0] * (n + 1)
        graph = [[] for _ in range(n + 1)]

        for employee in employees:
            index = employee.id
            value = employee.importance 
            
            val[index] = value
            graph[index] = employee.subordinates 
        
        self.mels = 0

        def dfs(index):
            self.mels += val[index]
            for nei in graph[index]:
                dfs(nei)

        dfs(id)
        return self.mels