https://leetcode.com/problems/reverse-bits/

----------------------------------------------------------------------------------------------

Problem Statement:
In this problem, we have to reverse bits of a given 32 bits unsigned integer.

----------------------------------------------------------------------------------------------

Appraoch:
We can reverse bits of a given number by iterating over all bits of the given number and adding the bits in the reverse order. To reverse the bits, we can use a variable and left shift it by 1 in each iteration. We can then add the last bit of the given number to the reversed number by performing an AND operation with the last bit of the given number. Once we add the last bit of the given number, we can right shift the given number by 1 to remove the last bit.

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            res ^= n & 1
            n >>= 1 
            
        return res

Complexity Analysis

-> Time complexity: O(32)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
