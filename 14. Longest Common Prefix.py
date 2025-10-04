'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        solution_value = []
        for index, char in enumerate(strs[0]):
            for word in strs:
                if index > len(word)-1:
                    return solution_value
                if word[index] != char:
                    return solution_value
                if word == strs[-1]:
                    solution_value.insert(index, char)
                
        return solution_value


assert Solution().longestCommonPrefix(["flower","flower","flower","flower"]) == "flower"
assert Solution().longestCommonPrefix(["flower","flow","fliwght"]) == "fl"
assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""

