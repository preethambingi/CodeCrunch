https://leetcode.com/problems/counting-bits/

----------------------------------------------------------------------------------------------

Problem Statement:
Given an integer n, we have to return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

----------------------------------------------------------------------------------------------

Approach 1: Naive Approach

In this method, we iterate through the integers from 0 to n, then we calculate the number of 1's in every iteration (i.e., for each i from 0 to n we calculate the number of 1's and store the results in the array.

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n + 1):
            c = 0
            while i:
                i = i & (i-1)
                c += 1
            res.append(c)
        return res

Complexity Analysis

-> Time complexity: O(nlogn)
Since for n numbers we calculate the number of 1's which takes logn time.

-> Space complexity: O(n)
This is because we store the result array of length n + 1.

----------------------------------------------------------------------------------------------

Approach 2: Using Offset and Dynamic Programming

In this method, we introduce a concept called offset which is a power of 2, we use this offset to calculate the number of 1's based on the previously calculated results.

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) 
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = res[i - offset] + 1
        return res

Complexity Analysis

-> Time complexity: O(n)
Since, we only iterate the array once.

-> Space complexity: O(n)
This is because we store the result array of length n + 1.

----------------------------------------------------------------------------------------------

Approach 3: Using Bit Manipulation and Dynamic Programming

In this method, we use bit manipulation, the number of 1's in i will be number of 1's in i >> 1 (i.e., i // 2) and the last bit in i. we can use Right Shift(>>) and AND(&) operators to solve this.

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) 
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

Complexity Analysis

-> Time complexity: O(n)
Since, we only iterate the array once.

-> Space complexity: O(n)
This is because we store the result array of length n + 1.

----------------------------------------------------------------------------------------------
