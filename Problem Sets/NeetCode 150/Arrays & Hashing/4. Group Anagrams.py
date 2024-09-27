https://leetcode.com/problems/group-anagrams/

----------------------------------------------------------------------------------------------

Problem Statement:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

----------------------------------------------------------------------------------------------

Approach 1: Using Hash Table

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ag_d = defaultdict(list)

        for x in strs:
            ag = "".join(sorted(x))
            ag_d[ag].append(x)
            
        return list(ag_d.values())
      
Complexity Analysis

-> Time complexity: O(n * wlogw), w is the length of the longest string

-> Space complexity: O(n * w)
----------------------------------------------------------------------------------------------

Approach 2: Using Hash Table and Counting Sort

class Solution:
    def countingSort(self, str: str) -> str:

        count_array = [0] * 26
        for i in str:
            count_array[ord(i) - ord('a')] += 1

        ss = ""
        for i in range(26):
            ss += (chr(i+ord('a'))) * count_array[i]
        
        return ss

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ag_d = defaultdict(list)

        for x in strs:
            ag = "".join(sorted(x))
            ag_d[ag].append(x)
            
        return list(ag_d.values())
      
Complexity Analysis

-> Time complexity: O(n * w), w is the length of the longest string

-> Space complexity: O(n * w)

----------------------------------------------------------------------------------------------
