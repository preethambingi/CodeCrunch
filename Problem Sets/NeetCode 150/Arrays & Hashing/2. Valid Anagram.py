https://leetcode.com/problems/valid-anagram/

----------------------------------------------------------------------------------------------

Problem Statement:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

----------------------------------------------------------------------------------------------

Approach 1: Using Sorting

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)

Complexity Analysis

-> Time complexity: O(nlogn)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Appraoch 2: Hash Table (Using array)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = [0] * 26

        for x in s:
            count[ord(x) - ord('a')] += 1

        for x in t:
            count[ord(x) - ord('a')] -= 1
         
        for c in count:
            if c != 0:
                return False
    
        return True

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Appraoch 3: Hash Table (Without Arrray)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = defaultdict(int)

        for x in s:
            count[x] += 1
        
        for x in t:
            count[x] += 1
        
        for value in count.values():
            if value != 0:
                return False
        
        return True
      
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)
----------------------------------------------------------------------------------------------
