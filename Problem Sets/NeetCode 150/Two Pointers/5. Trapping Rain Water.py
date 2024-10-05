https://leetcode.com/problems/trapping-rain-water/

----------------------------------------------------------------------------------------------

Problem Statement:

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

----------------------------------------------------------------------------------------------

Approach:

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

Complexity Anlysis:

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
