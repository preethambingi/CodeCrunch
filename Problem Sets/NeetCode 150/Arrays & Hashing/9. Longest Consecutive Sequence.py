https://leetcode.com/problems/longest-consecutive-sequence/

----------------------------------------------------------------------------------------------

Problem Statement:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

----------------------------------------------------------------------------------------------

Approach 1: Using Sorting [TLE]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        longest = 0
        if n == 1:
            return 1
        for i in range(1, n):
            length = 0
            while i < n and (nums[i] == nums[i-1] + 1 or nums[i] == nums[i-1]):
                if nums[i] == nums[i-1]:
                    i+=1
                    continue
                length += 1
                i += 1
            longest = max(longest, length + 1)
                    
        return longest

Complexity Analysis

-> Time complexity: O(nlogn)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Appraoch 2: Union Find (Unordered set)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        longest = 0
        length = 0
        for n in nums:
            if (n-1) not in numsSet: # eqvivalent to find function 

                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
                length = 0
            
        return longest

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)
----------------------------------------------------------------------------------------------
