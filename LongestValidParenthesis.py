"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring
.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output:

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = 0
        start = -1  # this keeps track of the position before a valid pair starts

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # store the index of '('
            else:
                if stack:
                    stack.pop()
                    if stack:
                        result = max(result, i - stack[-1])
                    else:
                        result = max(result, i - start)
                else:
                    start = i  # reset start if no matching '('

        return result
