class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t) // in build function to do the below implementation
    
        # return sorted(s) == sorted(t) // without memory
    
        if len(s) != len(t):
            return False
        
        slist, tlist = {}, {}
        for i in range(len(s)):
            slist[s[i]] = 1 + slist.get(s[i], 0)
            tlist[t[i]] = 1 + tlist.get(t[i], 0)

        for i in s:
            if slist[i] != tlist.get(i,0):
                return False
        return True
    
solution = Solution()
print(solution.isAnagram("JAR", "CAR"))