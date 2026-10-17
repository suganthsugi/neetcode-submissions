class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return 0
        cost.append(0)
        s1, s2 = cost[0], cost[1]

        for i in range(2, len(cost)):
            s1, s2 = s2, min(s1, s2)+cost[i]
        
        
        
        return s2