https://leetcode.com/problems/missing-number/

------------------------------------------------------------------------------------------------

Problem Statement:

Given an array nums containing n distinct numbers in the range [0, n], we must return the only number in the range that is missing from the array.

------------------------------------------------------------------------------------------------

Approach 1: SUM

In this method, we calcuate the natural sum and then we iterate the list and subtract each number to find the missing number.
  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = (n * (n + 1)) // 2
        for i in nums:
            res -= i
        return res

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

------------------------------------------------------------------------------------------------

Approach 2: XOR

In this method, we use XOR operator to find the missing number. We utilize A ^ A = 0 property.
  
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

------------------------------------------------------------------------------------------------

Appraoch 3: Binary Search (This works better if the array is pre-ordered)

In this method, first we sort the array since the array is not ordered. Then we use the Binary Search to find the missing number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        mid = (left + right) // 2

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        
        return left
      
Complexity Analysis

-> Time complexity: O(nlogn)
Complexity is nlogn because we sort the array.

-> Space complexity: O(1)

------------------------------------------------------------------------------------------------
