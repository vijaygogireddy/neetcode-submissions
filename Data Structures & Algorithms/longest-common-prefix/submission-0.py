class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        # lexicographically smallest and largest strings 
        # will expose the maximum difference in their prefixes

        first = strs[0]
        last = strs[-1]

        i = 0

        while i < min(len(first), len(last)) and first[i] == last[i]:
            i += 1

        return first[:i]



        '''
        l = r = 0

        n = len(min(strs))
        m = len(strs)
        
        '''