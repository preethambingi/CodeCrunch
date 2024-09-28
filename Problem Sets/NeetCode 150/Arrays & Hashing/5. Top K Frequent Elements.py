https://leetcode.com/problems/top-k-frequent-elements/

----------------------------------------------------------------------------------------------

Problem Statement:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

----------------------------------------------------------------------------------------------

Approach 1: Using Hashmap and Sorting

Complexity Analysis

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        count = sorted(count.items(), key = lambda x: x[1])
        most_freq_elements = count[::-1]
        res = [num for num, _ in most_freq_elements[:k]]
        
        return res
      
-> Time complexity: O(nlogn)

-> Space complexity: O(n)

----------------------------------------------------------------------------------------------

Approach 2: Using Priority Queue (Heapify)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
        heap = [[-freq, num] for num, freq in count.items()]
        heapify(heap)

        ans = []

        for i in range(k):
            _, num = heappop(heap)
            ans.append(num)

        return ans
      
Complexity Analysis

-> Time complexity: O(K * logn)

-> Space complexity: O(n)

---------------------------------------------------------------------------------------------

Approach 3: Using Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            res.extend(bucket[i])

            if len(res) >= k:
                return res[:k]
            
        return []
      
Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)

----------------------------------------------------------------------------------------------
