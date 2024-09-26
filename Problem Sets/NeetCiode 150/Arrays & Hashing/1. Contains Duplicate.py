https://leetcode.com/problems/contains-duplicate/

----------------------------------------------------------------------------------------------

Problem Statement:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
  
----------------------------------------------------------------------------------------------

Approach 1: Brute Force

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False

Complexity Analysis

-> Time complexity: O(n^2)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Approach 2: Using Sorting 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
            
        return False
      
Complexity Analysis

-> Time complexity: O(nlogn)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Appraoch 3: Using Hash Table

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        
        return False
        
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)

----------------------------------------------------------------------------------------------
