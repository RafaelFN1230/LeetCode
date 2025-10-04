'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1: return 0
        res = 0
        vis = [False] * 26

        left = 0
        right = 0

        while right < len(s):
            x= s[right]
            y = ord(s[right])
            z = ord(s[right]) - ord('a')
            
            while vis[ord(s[right]) - ord('a')]:
                vis[ord(s[left]) - ord('a')] = False
                left += 1   
            vis[ord(s[right]) - ord('a')] = True
            res = max(res, right - left + 1)
            right += 1

        return res
teste = Solution()

print(teste.lengthOfLongestSubstring("   ")) # 3
print(teste.lengthOfLongestSubstring("abcabcbb")) # 3
print(teste.lengthOfLongestSubstring("bbbbb")) # 1
print(teste.lengthOfLongestSubstring("pwwkew")) # 3
        