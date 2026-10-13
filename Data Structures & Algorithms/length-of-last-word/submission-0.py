class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)
        c = 0
        while i > 0 and not s[i-1].isalnum():
            i -= 1
        while i > 0 and s[i-1].isalnum():
            c += 1
            i -= 1
        return c
        
