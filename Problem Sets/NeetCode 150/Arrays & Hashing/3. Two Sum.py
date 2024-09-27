https://leetcode.com/problems/two-sum/

----------------------------------------------------------------------------------------------

Problem Statement:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

----------------------------------------------------------------------------------------------

Approach 1: Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return -1

Complexity Analysis

-> Time complexity: O(n^2)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Approach 2: Using Hashmap

As we iterate and add elements to the hash table, we simultaneously check if the complement of the current element is already present in the hash table. If the complement is found, we have a solution and can immediately return the indices.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i

        return []

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)
----------------------------------------------------------------------------------------------
