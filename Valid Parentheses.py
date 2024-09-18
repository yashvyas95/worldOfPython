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
#print(solution.isValid("()"))       # Output: True
#print(solution.isValid("()[]{}"))   # Output: True
#print(solution.isValid("(]"))       # Output: False

# Time Complexity : O(n)
# Space Complexity : O(n)

"""

Analysis:

    Queue 1 : What variations can be done on the problem.
    
    
            Parellel Questions:
                1. Print All the pairs of valid parenthesis combinations if n is given 
                2. Print All the  pairs of valid parenthesis combinations if k type of braces are given

"""


import itertools

class AlternateSolution:
    def allPossibleValidCombinations(self, s: str) -> list[str]:
        # Generate all permutations of the string
        permutations = itertools.permutations(s)
        
        # Convert permutations from tuples to strings
        perm_strings = {''.join(p) for p in permutations}
        
        # Function to check if a string has valid parentheses
        def is_valid_parentheses(s: str) -> bool:
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        
        # Filter valid permutations
        valid_combinations = [p for p in perm_strings if is_valid_parentheses(p)]
        
        # Print valid combinations
        print(valid_combinations)
        return valid_combinations

# Example usage
x = [2, 2, 7, 7, 11, 15]
y = 9
alternate_solution = AlternateSolution()
alternate_solution.allPossibleValidCombinations("((()))")

