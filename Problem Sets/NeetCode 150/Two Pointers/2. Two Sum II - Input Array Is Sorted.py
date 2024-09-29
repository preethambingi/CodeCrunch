https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

----------------------------------------------------------------------------------------------

Problem Statement:

[Medium]

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

---------------------------------------------------------------------------------------------

Approach 1: Using Dictionary

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in d:
                return [d[x] + 1, i + 1]
            d[numbers[i]] = i 

Complexity Analysis

-> Time compleity: O(n)

-> Space complexity: O(n)

----------------------------------------------------------------------------------------------

Approach 2: Two Pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

Complexity Analysis

-> Time compleity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
