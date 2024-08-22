from typing import List  # Ensure this import is included

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, b):
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] == ".":
                    for c in '123456789':
                        if self.isvalid(i, j, b, c):
                            b[i][j] = c
                            if self.solve(b):
                                return True
                            else:
                                b[i][j] = '.'
                    return False  # Ensure this is outside the inner for-loop
        return True
                
    def isvalid(self, row, col, b, c):
        for i in range(9):
            if b[row][i] == c:
                return False
            if b[i][col] == c:
                return False
            if b[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == c:
                return False
            
        return True
