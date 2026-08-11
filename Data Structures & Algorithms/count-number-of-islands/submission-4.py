class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        seen = set()

        if not grid: return 0

        rows = len(grid)
        cols = len(grid[0])


        
        def addseen(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0: return
            
            if (row, col) in seen or grid[row][col] == '0': return
            
            seen.add((row, col))
            addseen(row + 1, col)
            addseen(row - 1, col)
            addseen(row, col + 1)
            addseen(row, col - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in seen:
                    count += 1
                    addseen(r,c)


        return count
        