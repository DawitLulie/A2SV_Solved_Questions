class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for cost in costs:
            cost.append(abs(cost[0] - cost[1]))

        costs.sort(key=lambda x: x[2], reverse = True)

        n = len(costs) // 2
        cost = 0
        len1 = len2 = 0
        for a, b, d in costs:
            if a > b:
                if len2 < n:
                    cost += b
                    len2 += 1

                else:
                    cost += a
                    len1 += 1

                
            else:
                if len1 < n:
                    cost += a
                    len1 += 1
                else:
                    cost += b
                    len2 += 1

        return cost

        