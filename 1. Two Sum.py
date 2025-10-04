'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_positions = []
        for index, num in enumerate(nums):
            second_num = target - num 
            if second_num in nums[index+1:]:
                nums_positions.append(index)
                for index2 in range(len(nums)-1, index, -1):
                    x=nums[index2]
                    if nums[index2] == second_num and index != index2:
                        nums_positions.append(index2)
                        return nums_positions
            
teste = Solution()
print(teste.twoSum([2,7,11,10,8,15], 9)) # [0,3]
print(teste.twoSum([11,15,2,7], 9)) # [1,3]
print(teste.twoSum([3,3], 6)) # [0,1]
print(teste.twoSum([2,7,11,15], 9)) # [0,1]
print(teste.twoSum([11,2,15,7], 9)) # [1,3]
print(teste.twoSum([3,2,4], 6)) # [1,2]
        