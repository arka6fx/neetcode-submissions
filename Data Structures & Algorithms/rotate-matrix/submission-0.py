class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def transpose(matrix: List[List[int]]) -> None:
            rows = len(matrix)
            cols = len(matrix[0])

            for r in range(rows):
                for c in range(r + 1, cols):#upper triangle
                    matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

        def reverse(matrix: List[List[int]]) -> None:

            for row in range(len(matrix)):
                l = 0
                r = len(matrix) - 1
                while l < r:
                    temp = matrix[row][l]
                    matrix[row][l] = matrix[row][r]
                    matrix[row][r] = temp
                    l += 1
                    r -= 1

        transpose(matrix)
        reverse(matrix)

        