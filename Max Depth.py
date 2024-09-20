"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # Base case: if the tree is empty
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)  # Use self to call the method
        right_depth = self.maxDepth(root.right)  # Use self to call the method
        
        # Return the maximum depth
        return max(left_depth, right_depth) + 1