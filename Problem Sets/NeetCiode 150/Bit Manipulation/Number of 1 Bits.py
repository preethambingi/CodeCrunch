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

Complexity Analysis

-> Time complexity: O(number of bits)
Because we iterate over all the bits present in the number.

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Approach 2: Unset the Rightmost Set Bit

In the method, we will repeatedly unset the rightmost set bit using n = n & (n - 1), by this we can directly count how many set bits are there.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            n = n & (n - 1)
            count += 1
        
        return count

Complexity Analysis

-> Time complexoty: O(number of set bits)
Since for every iteration we will unset one bit.

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------

Approach 3: Using Modulo and Division

In this method, first we will check whether the LSD is set or not, it its set then we will increment the count. Then we will divide the number by two, this will automatically right shift the number by one bit every time.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1 == 1:
                count += 1
            n //= 2
        
        return count

Complexity Analysis

-> Time complexoty: O(logn)
Since for every iteration we half the number.

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
