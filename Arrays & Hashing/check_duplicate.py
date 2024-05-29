
nums = [1,4,6,2,2]

# Approach 1: By conveting it into set and check length of new set and provided nums
# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         mySet = set(nums)
#         if len(mySet) < len(nums):
#             return True
#         return False
  
# Approach 2 By adding all elements in set and while adding check If already present
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)  
        return False
    
solution = Solution()

print(solution.hasDuplicate(nums))