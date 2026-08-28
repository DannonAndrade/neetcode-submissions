class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        islands = 0

        def fill(cord):

            row = cord[0]
            col = cord[1]

            seen.add((row, col))

            #top
            if row > 0 and grid[row - 1][col] == "1" and (row - 1, col) not in seen:
                fill([row - 1, col])
            #bottom
            if row < len(grid) - 1 and grid[row + 1][col] == "1" and (row + 1, col) not in seen:
                fill([row + 1, col])
            #left
            if col > 0 and grid[row][col - 1] == "1" and (row, col - 1) not in seen:
                fill([row, col - 1])
            #right
            if col < len(grid[0]) - 1 and grid[row][col + 1] == "1" and (row, col + 1) not in seen:
                fill([row, col + 1])


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] != "0":
                    fill([row, col])
                    islands += 1
            
        return islands
                


        


        