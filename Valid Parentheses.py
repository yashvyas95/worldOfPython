"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false


"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a mapping of closing brackets to opening brackets
        matching = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            if char in matching:
                # If stack is not empty, pop the top element, else assign dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element is the corresponding opening bracket
                if matching[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, it means all brackets were matched
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False
