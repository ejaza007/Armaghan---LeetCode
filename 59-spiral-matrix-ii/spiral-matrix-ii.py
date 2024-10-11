from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the initial boundaries of the matrix
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        current_number = 1
        
        while current_number <= n * n:
            # Fill from left to right across the top row
            for i in range(left, right + 1):
                matrix[top][i] = current_number
                current_number += 1
            top += 1

            # Fill from top to bottom down the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = current_number
                current_number += 1
            right -= 1

            # Fill from right to left across the bottom row if within bounds
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = current_number
                    current_number += 1
                bottom -= 1

            # Fill from bottom to top up the left column if within bounds
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = current_number
                    current_number += 1
                left += 1

        return matrix
