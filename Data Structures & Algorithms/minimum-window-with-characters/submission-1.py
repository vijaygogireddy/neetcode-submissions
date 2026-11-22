class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        if slen < tlen: return ''

        tmap = Counter(t)
        smap = {}

        min_window = float('inf')
        need = len(tmap)
        have = 0

        '''
        def isValidWindow():
            # O(52) worst
            for val in tmap:
                if val not in smap: return False
                elif smap[val] < tmap[val]: return False
            return True
        '''
        l = 0
        for r in range(slen):
            rchar = s[r]
            smap[rchar] = smap.get(rchar, 0) + 1

            if rchar in tmap and smap[rchar] == tmap[rchar]:
                have += 1

            # while isValidWindow():
            while have == need:
                w = r - l + 1
                if w < min_window:
                    min_window = w
                    start_index = l
                
                lchar = s[l]
                # if smap[lchar] == 1: del smap[lchar]
                if lchar in tmap and smap[lchar] == tmap[lchar]:
                    have -= 1
                
                smap[lchar] -= 1
                l += 1
        
        if min_window == float('inf'): return ''
        
        return s[start_index : start_index + min_window]

           