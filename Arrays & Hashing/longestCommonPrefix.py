# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""  # default response

        # you can choose any one string and compare the other string, so here we are choosing flower at first
        # then comparing next other string each matching character and adding in res
        # loop on first element, flower i.e 6
        # then looping on flow and flight i.e line 17 and checking each character in all the adding 
        # If character is same in each word, add in res, otherwise return
        # But make sure to check len of each string because we are iterating till 6 but flow has only 4 character
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
        