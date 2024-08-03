class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if not matrix or not matrix[0]:
            return 
        n= len(matrix[0])
        m= len(matrix)
        nn= n*[False]

        mm= m*[False]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    mm[i]=True
                    nn[j]=True
        
        for i in range(m):
            for j in range(n):
                if mm[i] or  nn[j]:
                    matrix[i][j] =0
        
        return matrix

        
