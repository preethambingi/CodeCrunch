https://leetcode.com/problems/single-number/

----------------------------------------------------------------------------------------------

Problem Explanation: 

We are given a non-empty array of integers nums, where every element appears twice except for one. We need to find that single one and return it.

----------------------------------------------------------------------------------------------

Approach 1: Using Dictionary (Hashmap)

The first method that comes up to the mind is storing the frequencies of the elements and then return the element with frequency 1.
We can use dictionaries in python to store the frequencies of the eements.
  
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for key, value in d.items():
            if value == 1: return key

Complexity Analysis

-> Time complexity: O(n)
The time complexity is O(n) because the traverse the entire list.
  
-> Space complexity: O(n)
The space required is O(n) because we store the frequencies of the all the nums list.

----------------------------------------------------------------------------------------------

Approach 2: Using Sorting

The second method that comes up to nind is using sorting. After sorting we traverse the list and check if one of the adjacent element is equal to current element. if it's not equal then we can return the element.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # since XOR with 0 returns same number 

        for i in nums:
            res ^= i # X^X = 0
        
        return res

Complexity Analysis:

-> Time complexity: O(nlogn)
The time complexxity is O(nlogn) because we are sorting the list which takes nlogn time.

-> Space complexity: O(1)
The space complexity is constant because we are not storing anything.

----------------------------------------------------------------------------------------------

Approach 3: Using Bitwise XOR Operator (Most Efficient Approach)

The best approach that comes to mind is using XOR operator. 
To get better understanding about how it works let's look at some XOR properties:
X ^ 0 = 0, X ^ X = 0, X ^ X ^ Y = Y

Using this properties we will solve the problem.

  class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 

        for i in nums:
            res ^= i
        
        return res

Complexity Analysis

-> Time complexity: O(n)
The time complexity is O(n) because the traverse the entire list.

-> Space complexity: O(1)
The space complexity is constant because we are not storing anything.

----------------------------------------------------------------------------------------------
