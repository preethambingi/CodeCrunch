https://leetcode.com/problems/reverse-integer/

------------------------------------------------------------------------------------------------

Problem Statement:

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

------------------------------------------------------------------------------------------------

Appraoch: Modulo and Division

In this problem, we have to return 0 If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1]. So before moving the digits place we have check whether we are in bounds by res > MAX // 10, we have to do the same for MIN.

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        res = 0
        while x:
            d = int(math.fmod(x, 10)) # (python dumb) -1 % 10 = 9
            x = int(x/10) # (python dumb) -1 // 10 = -1

          # here, we also checking the last bit
            if res > MAX // 10 or (res == MAX // 10 and d > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and d < MIN % 10):
                return 0
            res = (res * 10) + d

        return res

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        res = 0
        while x:
            d = int(math.fmod(x, 10)) # (python dumb) -1 % 10 = 9
            x = int(x/10) # (python dumb) -1 // 10 = -1
            res = (res * 10) + d
            if res > MAX or res < MIN:
                return 0
        
        return res

Complexity Analysis

-> Time complexity: O(logn)

-> Space complexity: O(1)
------------------------------------------------------------------------------------------------
