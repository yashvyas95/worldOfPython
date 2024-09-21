"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # Get the letter at the current position on the board
            letter = board[x][y]
            # Traverse the trie to the next node
            cur = root[letter]
            # Check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            # Mark the current position on the board as visited
            board[x][y] = '*'
            # Recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # Restore the original value of the current position on the board
            board[x][y] = letter
            # If the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)
                
        # Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Initialize a list to store the results
        res = []
        
        # Traverse the board and search for words
        for i in range(m):
            for j in range(n):
                # Check if the current letter is in the trie
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        # Return the list of results
        return res
        
        """
        Time Complexity
The time complexity of the algorithm depends on two main factors:

Building the Trie from the list of words.
Performing DFS on each cell of the board.
1. Building the Trie
Inserting each word into the Trie involves traversing each character of the word. Let:
W be the total number of words.
L be the average length of each word.
The total time to insert all words into the Trie is O(W * L).
2. Performing DFS
For each cell in the board, you initiate a DFS, exploring in four possible directions (up, down, left, right).
In the worst case, you could potentially explore every cell of the board up to the length of the longest word. If the longest word has length L, and the board has dimensions m x n, then for each starting cell, the DFS could theoretically explore O(L) cells in depth.
Thus, for every cell (i, j) in the board, the DFS takes O(4^L) time, where L is the length of the longest word (since each step in the DFS can branch in 4 directions: up, down, left, and right).

For an m x n board, you start a DFS from every cell, leading to a time complexity of O(m * n * 4^L) in the worst case.
Total Time Complexity
The total time complexity is the sum of the time for building the Trie and performing DFS:

Trie construction: O(W * L).
DFS traversal: O(m * n * 4^L).
Thus, the overall time complexity is:

O(W * L + m * n * 4^L).

However, in practice, pruning the Trie (removing nodes when they no longer lead to valid words) significantly reduces the number of branches in the DFS. As a result, the actual time spent is often much lower than the worst-case scenario.

Space Complexity
There are several components to the space complexity:

Trie Storage:

The Trie is built from all words, and each word contributes one node per character. For W words of average length L, the Trie occupies O(W * L) space.
Recursion Stack (DFS):

The DFS uses recursion to explore each cell. The depth of the recursion stack is bounded by the length of the longest word L. In the worst case, you may store up to L recursive calls on the stack.
Thus, the recursion stack uses O(L) space.
Board Modification:

The algorithm modifies the board in place (marking cells as visited with '*'), so no additional space is used for tracking visited cells.
Result Storage:

The results are stored in a list (res). In the worst case, the list will contain all the words from the input, so it uses O(W) space.
Total Space Complexity
The total space complexity is the sum of the space used by the Trie, the recursion stack, and the result storage:

Trie storage: O(W * L).
DFS recursion stack: O(L).
Result list: O(W).
Thus, the overall space complexity is:

O(W * L + L + W), which simplifies to O(W * L) (since L is generally much smaller than W * L).

Conclusion
Time Complexity: O(W * L + m * n * 4^L).
Space Complexity: O(W * L).
"""