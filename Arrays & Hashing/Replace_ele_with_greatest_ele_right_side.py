class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
    # Approach one: O(n*n)
    #    for i in range(len(arr)):
    #         temp = -1
    #         for j in range(i+1, len(arr)):
    #             temp = max(arr[j], temp)
    #         arr[i] = temp
    
    #    arr[len(arr) - 1] = -1
    #    return arr

    # Approach 2 with O(N) from reverse iterating
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
 
solution = Solution()
print(solution.replaceElements([17,18,5,4,6,1]))