class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        if slen < tlen: return ''

        tmap = Counter(t)
        smap = {}

        min_window = float('inf')

        def isValidWindow():
            # O(52) worst
            for val in tmap:
                if val not in smap: return False
                elif smap[val] < tmap[val]: return False
            return True
        
        l = 0
        for r in range(slen):
            smap[s[r]] = smap.get(s[r], 0) + 1

            while isValidWindow():
                w = r - l + 1
                if w < min_window:
                    min_window = w
                    start_index = l

                if smap[s[l]] == 1: del smap[s[l]]
                else: smap[s[l]] -= 1
                l += 1
        
        if min_window == float('inf'): return ''
        else:
            return s[start_index : start_index + min_window]

           