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


Why It’s Greedy
Locally Optimal Choices: At every step (row flips and column flips), we're making the best immediate decision:
For rows: Flip the row if it starts with 0, since this immediately maximizes the MSB.
For columns: Flip the column if it has more 0s than 1s, since this maximizes the number of 1s in that column, contributing to a higher overall score.
No Backtracking: Once a row or column is flipped, we do not need to revisit that decision. We're assuming that the choice made at each step is the best possible without needing to reconsider it later.
Greedy Optimality
Why this approach works: In this problem, the greedy approach is optimal because:
The first column contributes the most to the final score (being the most significant bit), so maximizing the number of 1s there is a clear step.
For other columns, each flip decision is independent of the rest, and flipping a column can only increase the score (if it results in more 1s).
Thus, this is a classic greedy algorithm where local optimizations lead to a globally optimal solution.

Time Complexity
O(m * n), where m is the number of rows and n is the number of columns, since we iterate over each element of the matrix once for both row and column flips.
In summary, this is a greedy algorithm because we're making decisions to maximize the score at each step, and these decisions are not revisited later. The approach works efficiently and ensures the best possible score.


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