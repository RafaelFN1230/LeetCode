'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}

        for n in nums:
            if n in elements:
                elements[n] += 1
            else:
                elements[n] = 1
            
            if elements[n] > len(nums)/2:
                return n

teste = Solution()
print(teste.majorityElement(nums = [3,2,3]))
print(teste.majorityElement(nums = [2,2,1,1,1,2,2]))