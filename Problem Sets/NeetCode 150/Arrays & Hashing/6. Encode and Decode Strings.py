https://leetcode.com/problems/encode-and-decode-strings/

----------------------------------------------------------------------------------------------

Problem Statement:

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
  
----------------------------------------------------------------------------------------------

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            ln = int(s[i:j])
            w = s[j+1: j + ln + 1]
            res.append(w)
            i = j + ln + 1

        return res

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(n)
----------------------------------------------------------------------------------------------
