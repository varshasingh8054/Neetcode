# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sTMap, tSMap = {}, {}
    
        for i in range(len(s)):
            if sTMap.get(s[i], 0) and t[i] != sTMap.get(s[i], 0):
                return False
            if tSMap.get(t[i], 0) and s[i] != tSMap.get(t[i], 0):
                return False

            sTMap[s[i]] = t[i]
            tSMap[t[i]] = s[i]

        return True
        
sol = Solution()
print(sol.isIsomorphic("egg", "add"))