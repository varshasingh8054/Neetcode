# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # count = 1
        # majEle = nums[0]
        # for i in range(1, len(nums)):
        #     if majEle == nums[i]:
        #         count+=1
        #     else:
        #         count-=1
        #         if count == -1:
        #             majEle = nums[i]
        #             count = 1
        
        # return majEle

        res, count = 0, 0 # neetCode

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))