"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""


# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         result = ListNode(-1)  # Dummy node to start the list
        anchor = result  # This will be used to build the new list
        i, j = list1, list2  # Set pointers to both lists

        # Loop through both lists while both have elements
        while i and j:
            if i.val <= j.val:
                anchor.next = ListNode(i.val)
                i = i.next  # Move to the next node in list1
            else:
                anchor.next = ListNode(j.val)
                j = j.next  # Move to the next node in list2
            anchor = anchor.next  # Move the anchor to the new node

        # If one list is exhausted, append the rest of the other list
        if i:  # If list1 still has elements
            anchor.next = i
        if j:  # If list2 still has elements
            anchor.next = j

        return result.next  # Return the merged list starting from the first real node
       
# Time Complexity=O(m+n)

       