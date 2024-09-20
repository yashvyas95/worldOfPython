"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.
 
 Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
    # Anagrams must be the same length
    if len(s) != len(t):
        return False
    
    # Sort both strings and compare them
    return sorted(s) == sorted(t)    
        
        # O (nlogn)
        
from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    # Anagrams must be the same length
    if len(s) != len(t):
        return False
    
    # Count character frequencies in both strings
    return Counter(s) == Counter(t)        
    
    # o (n)