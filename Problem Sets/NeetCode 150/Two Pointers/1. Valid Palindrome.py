https://leetcode.com/problems/valid-palindrome/

----------------------------------------------------------------------------------------------

Problem Statement:

[Easy]

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

----------------------------------------------------------------------------------------------

Appraoch:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
