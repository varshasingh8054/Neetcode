# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

from typing import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Create a obj for first string and then one by one start comparing with other string 
        # create a obj for other string and compare with initial string
        # If extra key is found in initial object then delete that key or if less value is find for the key
        # then update the key
        # counter[i] = min(currentCounter[i], counter[i]) update and delete both can be done by this
        # If it doesn't found key in object it will return 0, example counter['z'] = 0

        counter = Counter(words[0])

        for w in words:
            currentCounter = Counter(w)
            for i in counter:
                counter[i] = min(currentCounter[i], counter[i])

        res = []
        for i in counter:
            for j in range(counter[i]):
                res.append(i)
            
        return res

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))