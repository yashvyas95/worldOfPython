"""

You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.



Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
Example 2:

Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4
"""
from typing import List


class Trie:
    def __init__(self):
        self.score = 0
        self.children = {}

    def add(self, s: str, i: int):
        if (i): self.score += 1
        if (i == len(s)): return
        if (not self.children.get(s[i])): self.children[s[i]] = Trie()
        self.children[s[i]].add(s, i + 1)

    def dfs(self, s: str, i: int):
        if (i == len(s)): return self.score
        return self.score + self.children[s[i]].dfs(s, i + 1)


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word, 0)
        res = []
        for word in words:
            res.append(trie.dfs(word, 0))
        return res


s = Solution()
s.sumPrefixScores(["abcd"])