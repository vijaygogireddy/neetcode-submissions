class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        m, n = len(s), len(t)

        while i < m:
            while s[i] != t[j]:
                j += 1
                if j == n:
                    return False
            if s[i] == t[j]:
                i, j = i+1, j+1

            if i == m:
                return True

        return False
            


