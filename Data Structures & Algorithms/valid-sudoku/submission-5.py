class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                square = (r//3,c//3)
                if val == ".":
                    continue
                if val in cols[c] or val in rows[r] or val in squares[square]: return False

                cols[c].add(val)
                rows[r].add(val)
                squares[square].add(val)
        
        return True
        