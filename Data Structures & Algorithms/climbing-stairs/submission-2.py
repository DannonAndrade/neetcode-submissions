class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {1: 1, 2: 2}

        def dfs(stair: int):
            if stair in memo:
                return memo[stair]
            else:
                memo[stair] = dfs(stair - 1) + dfs(stair - 2)
                return memo[stair]
        
        return dfs(n)

        
        