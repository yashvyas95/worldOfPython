"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Use two-pointer technique to compare characters from both ends
    i, j = 0, len(s) - 1
    
    while i < j:
        if s[i] != s[j]:
            return False  # Not a palindrome if characters don't match
        i += 1
        j -= 1
    
    return True  # If loop completes, it's a palindrome 


Solution = Solution()
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("race a car"))
print(Solution.isPalindrome(" "))

# O(n)


        