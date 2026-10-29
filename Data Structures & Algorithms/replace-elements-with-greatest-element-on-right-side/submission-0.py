class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        res = [-1] * n

        for i in range(n-1):
            res[i] = max(arr[i+1:])

        return res