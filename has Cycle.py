"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

"""

class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    
    while fast and fast.next:  # Ensure fast and fast.next are not None
        slow = slow.next        # Move slow pointer by 1 step
        fast = fast.next.next   # Move fast pointer by 2 steps
        
        if slow == fast:        # Check if they meet
            return True
            
    return False  # No cycle found