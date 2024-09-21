"""

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, curr = None, head
        while curr:
            oldNext = curr.next  # Store the next node
            curr.next = temp     # Reverse the current node's pointer
            temp = curr          # Move `temp` to current node
            curr = oldNext       # Move to the next node in the original list
        return temp  # `temp` is the new head of the reversed list
