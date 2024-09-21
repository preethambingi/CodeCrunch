https://leetcode.com/problems/number-of-1-bits/

----------------------------------------------------------------------------------------------

Problem Explanation:

The Hamming Weight of an integer is the number of '1' bits in its binary representation. Given a non-negative integer n, the task is to determine how many of its bits are set to '1'.

----------------------------------------------------------------------------------------------

Approach 1: Iterating Over All Bits

In this method we will check if the least significant bit is set or not (n & 1 == 1), then we will increment the count whenever we encounter a set bit. For the next iteration we will right shift the number by one bit (n >> 1).

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        
        return count

Complexity Analysis:

Time complexity: O(number of bits)




