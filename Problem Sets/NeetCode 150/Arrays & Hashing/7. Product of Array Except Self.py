https://leetcode.com/problems/product-of-array-except-self/

----------------------------------------------------------------------------------------------

[Medium] 

Problem Statement: 

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
  
----------------------------------------------------------------------------------------------

Approach 1: Brute Force [TLE]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            res.append(product)

        return res
      
Complexity Analysis

-> Time complexity: O(n^2)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Approach 2: Dynamic Programming (Tabulation)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, n):
            prefix[i] *= prefix[i-1] *  nums[i-1]

        for i in range(n-2, -1, -1):
            postfix[i] *= postfix[i+1] *  nums[i+1]

        for i in range(n):
            res[i] = prefix[i] * postfix[i]
            
        return res
      
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)

----------------------------------------------------------------------------------------------

Approach 3: Dynamic Programming (Space Optimization)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * len(nums)
        
        for i in range(1, n):
            res[i] *= res[i-1] * nums[i-1]
        
        pd = 1
        for i in range(n-1, -1, -1):
            res[i] *= pd
            pd *= nums[i]

        return res
      
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
