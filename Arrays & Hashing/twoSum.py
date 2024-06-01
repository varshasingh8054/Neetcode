



1234567891011
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # My Code-----------------------------
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i

        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if hashmap.get(diff, 0) and i!=hashmap[diff]:
        #         return [i, hashmap[diff]]
            
        # neet code
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

solution = Solution()
print(solution.twoSum([1,3,4,2], 6))
print(solution.twoSum([5,5], 10))