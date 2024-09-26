https://leetcode.com/problems/sum-of-two-integers/

------------------------------------------------------------------------------------------------

Problem Statement:

Given two integers a and b, we hve to return the sum of the two integers without using the operators + and -.

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

------------------------------------------------------------------------------------------------

Approach 1: Using XOR (additon) and AND (carry) operators with MASK and MAX

In this method, we have to note that masking removes the 2's compliment, so we have to manually convert the integer to proper representation.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
    
        while (b):
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        
        return a if a <= MAX else ~(a ^ MASK) 

Here, if a > MAX means it is a negative number (-20 wil be representated as 11101100 in 8-bit representation, since we used masking inside the loop -20 lost its 2's complement so python wont be able to recognize that it is a negative number instead it returns the integer representation of this 11101100 binray representation which we will be a very large number. So we will manually convert it into negative number.

Example:
-20 -> 11101100
11101100 ^ MASK -> 00010011
~(00010011) -> -Obx00010100 -> -20

Complexity Analysis

-> Time Complexity: O(32)

-> Space Complexity: O(1)

------------------------------------------------------------------------------------------------

Approach 2: Using XOR (additon) and AND (carry) operators

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        
        while (b & MASK):
            carry = ((a & b) << 1)
            a = (a ^ b)
            b = carry
    
        return a & MASK if b else a

Here, in this method we the two integers have opposite signs then the carry will go on until it exceeds the 32 bit representation. Usually we ignore this exceeded carry but python considers this and returns a huge number. To handle this overflow we have to use mask.

Example: -1 + 1
-1 -> 11111111
1  -> 00000001
-----------------
add -> 11111110
carry -> 00000010
-----------------
add -> 11111100
carry -> 00000100
-----------------
.
.
.
-----------------
add -> 10000000
carry -> 10000000
-----------------
add -> 1<->00000000 (Exceeded)
carry -> 1<->00000000
-----------------

Complexity Analysis

-> Time Complexity: O(32)

-> Space Complexity: O(1)

------------------------------------------------------------------------------------------------
