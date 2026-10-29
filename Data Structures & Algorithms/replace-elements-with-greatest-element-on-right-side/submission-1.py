class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # O(n)
        n = len(arr)
        curr_max = -1
        for i in range(n-1, -1, -1):

            temp = arr[i]

            arr[i] = curr_max

            curr_max = max(curr_max, temp)

        return arr


        '''
        # O(n^2)
        n = len(arr)
        res = [-1] * n

        for i in range(n-1):
            res[i] = max(arr[i+1:])

        return res
        '''