from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        set pointers in nums
         for i in range(len(nums)):  # first
            for j in range(i+1, len(nums)):  # second on right
#               if both pointer ints = target
                if nums[i] + nums[j] == target:
#                   return nums indexes only
                    return [i, j] 
                
                
                
                
                
                
                
                
# Test cases below 

input_list = [2,8,12,15]
test1 = Solution()
print(test1.twoSum(input_list, 20))
# [1, 2]

# input_list_2 = [2,7,11,15]
# test2 = Solution()
# print(test2.twoSum(input_list_2, 9))
# [0, 1]
