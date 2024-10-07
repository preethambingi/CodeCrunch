https://leetcode.com/problems/longest-substring-without-repeating-characters/

----------------------------------------------------------------------------------------------

Given a string s, find the length of the longest substring without repeating characters.

----------------------------------------------------------------------------------------------

Approach:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            res = max(res, i - l + 1)
        return res
      
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
