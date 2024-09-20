"""
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None  # Return immediately if the tree is empty
    
    q = deque()  # Use deque for efficient queue operations
    q.append(root)
    
    while q:
        current = q.popleft()  # Get the current node from the front of the queue
        
        # Swap the left and right children
        current.left, current.right = current.right, current.left
        
        # If the left child exists, add it to the queue for further processing
        if current.left:
            q.append(current.left)
        
        # If the right child exists, add it to the queue for further processing
        if current.right:
            q.append(current.right)
    
    return root  # Return the root of the inverted tree   
    
    
 # O(n) both
 
 
 