"""
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.

"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Helper function to build the KMP table
        def build_kmp_table(pattern):
            n = len(pattern)
            kmp_table = [0] * n
            j = 0  # length of the previous longest prefix suffix
            # Build the KMP table
            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]:
                    j = kmp_table[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                kmp_table[i] = j

            return kmp_table

        # Edge case: If the string is empty or already a palindrome
        if not s or s == s[::-1]:
            return s

        # Create a new string by combining s and its reverse with a separator
        combined = s + "#" + s[::-1]

        # Build the KMP table for this combined string
        kmp_table = build_kmp_table(combined)

        # The length of the longest palindrome prefix is given by the last value in the KMP table
        longest_palindromic_prefix_length = kmp_table[-1]

        # We need to add the remaining part of the string (after the palindrome prefix) reversed at the beginning
        remaining_part = s[longest_palindromic_prefix_length:]
        result = remaining_part[::-1] + s

        return result

solution = Solution()
s = "aacecaaa"
print(solution.shortestPalindrome(s))  # Output: "aaacecaaa"

s = "abcd"
print(solution.shortestPalindrome(s))  # Output: "dcbabcd"