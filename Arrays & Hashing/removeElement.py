# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1

        return count

sol = Solution()
print(sol.removeElement([3,2,2,3], 3))