class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        islands = 0

        def dfs(r, c):
            if grid[r][c] != "1" or (r,c) in seen:
                return 
            else:
                seen.add((r,c))
                if r + 1 < len(grid):
                    dfs(r + 1, c)
                if r - 1 > -1:
                    dfs(r - 1, c)
                if c + 1 < len(grid[0]):
                    dfs(r, c + 1)
                if c - 1 > -1:
                    dfs(r, c - 1)
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if (r,c) in seen or grid[r][c] == "0":
                    continue
                else:
                    islands += 1
                    dfs(r,c)

        return islands
        