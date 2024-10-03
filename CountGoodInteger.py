"""
Here's the plan:

We determine pals_left the list of the left sides of the possible palindromes.

For each left side pal_left, we determine pal_rght, which we join to determine pal, a palindrome.

We check whether pal is k-palindromic. If so, we add its sorted string to the set k_pals. (We sort to avoid redundant palindromes.)

We use combinatorics to count the rearrangements for each k_pal, and return the sum of these counts as the asnswer.


Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468



"""


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        if n == 1: return 9 // k
        k_pals, ans = set(), 0

        pals_left = product(*[digits[1:]] + [digits] * ((n - 1) // 2))  # <-- 1

        for pal_left in pals_left:

            pal_rght = pal_left[::-1][n % 2:]  # <-- 2
            pal = ''.join(((*pal_left, *pal_rght)))

            if int(pal) % k == 0:  # <-- 3
                k_pals.add(''.join(sorted(pal)))

        for k_pal in k_pals:
            ctr = Counter(k_pal)  # <-- 4
            denom = reduce(mul, map(factorial, ctr.values()))
            ans += factorial(n) * (n - ctr['0']) // (denom * n)

        return ans