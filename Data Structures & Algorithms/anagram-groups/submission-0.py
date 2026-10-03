class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # nlogn - sorting
        # res = defaultdict(list)
        res = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())


        
        '''
        countArr = [[0] * 26] * len(strs)
        resList = [[]]

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                countArr[i][ord(strs[i][j])-ord('a')] += 1

        
        return resList
        '''