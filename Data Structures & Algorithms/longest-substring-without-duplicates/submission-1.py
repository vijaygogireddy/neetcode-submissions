class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        # if n < 2: return n

        maxLen = 0
        hashset = set()
        i = 0
        
        for j in range(n):
            # hashset.add(s[i])
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1
            hashset.add(s[j])
            maxLen = max(maxLen, j-i+1)

            
        return maxLen