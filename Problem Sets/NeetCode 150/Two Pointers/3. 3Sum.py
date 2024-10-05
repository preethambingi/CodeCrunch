https://leetcode.com/problems/3sum/

----------------------------------------------------------------------------------------------

Problem Statement:

[Medium]

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

----------------------------------------------------------------------------------------------

Appraoch:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        start, n  = 0, len(nums)

        while start < n - 1:
            l, r = start + 1, n - 1

            while l < r:
                threeSum = nums[start] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[start], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1 
            start += 1
            
            while start < n - 1 and nums[start-1] == nums[start]:
                start += 1
        return res

Complexity Analysis

Time complexity: O(nlogn)

Space complexity: O(1)

----------------------------------------------------------------------------------------------
