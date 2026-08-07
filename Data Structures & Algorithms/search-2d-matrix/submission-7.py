class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lrow = 0
        rrow = len(matrix) - 1

        while lrow <= rrow:

            mrow = (lrow + rrow) // 2
            row = matrix[mrow]

            if target < row[0]:
                rrow = mrow - 1
            elif target > row[-1]:
                lrow = mrow + 1
            else:

                lcol = 0
                rcol = len(row) - 1

                while lcol <= rcol:
                    mcol = (lcol + rcol) // 2
                    
                    if row[mcol] == target: return True
                    elif row[mcol] > target:
                        rcol = mcol - 1
                    else:
                        lcol = mcol + 1
                return False
                        
            
        return False
            
        