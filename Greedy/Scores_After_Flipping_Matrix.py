"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1

"""


from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Step 1: Ensure that every row starts with a 1 by flipping rows if necessary
        for row in grid:
            if row[0] == 0:
                # Flip the row if it starts with 0
                for j in range(len(row)):
                    row[j] = 1 - row[j]  # Flip each element (0 -> 1, 1 -> 0)

        # Step 2: Maximize the score by flipping columns to maximize the number of 1's
        rows, cols = len(grid), len(grid[0])
        for j in range(1, cols):
            ones_count = sum(grid[i][j] for i in range(rows))  # Count 1's in column j
            if ones_count < rows / 2:  # If there are more 0's than 1's, flip the column
                for i in range(rows):
                    grid[i][j] = 1 - grid[i][j]  # Flip each element in the column

        # Step 3: Calculate the final score
        score = 0
        for row in grid:
            # Convert each row from binary to a decimal number and add it to the score
            row_value = int("".join(map(str, row)), 2)  # Convert binary list to string, then to integer
            score += row_value

        return score

Solution = Solution()
Solution.matrixScore( [[0,0,1,1],[1,0,1,0],[1,1,0,0]])