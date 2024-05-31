class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # count = 0 //Mycode
        # j=0 
        # for i in range(len(s)):
        #     while(j<len(t)):
        #         if s[i] == t[j]:
        #             count = count + 1
        #             j=j+1
        #             break
        #         j = j+1
        
        # if count == len(s):
        #     return True
        # return False

        # Neetcode
        # class Solution:
        # def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))
print(solution.isSubsequence("axc", "ahbgdc"))