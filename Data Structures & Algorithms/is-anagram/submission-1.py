class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countArr1 = [0] * 26
        countArr2 = [0] * 26

        if len(s) != len(t): return False
        for i in range(len(s)):
            countArr1[ord(s[i]) - ord('a')] +=1
            countArr2[ord(t[i]) - ord('a')] +=1


        return True if countArr1 == countArr2 else False