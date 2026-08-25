class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        base cases:
        first floor
        second floor
        '''
        mincost = {0: cost[0], 1: cost[1]}
        
        def dfs(i):
            if i in mincost:
                return mincost[i]
            else:
                mincost[i] = min(dfs(i - 1), dfs(i - 2)) + cost[i]
                return mincost[i]
        
        
        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))

            

        