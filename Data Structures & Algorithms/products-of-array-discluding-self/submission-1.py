class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # if Counter(nums)[0] > 1:
        #     return [0] * n

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix = nums[i] * prefix

        postfix = 1
        for j in range(n-1, -1, -1):
            res[j] = res[j] * postfix
            postfix = nums[j] * postfix

        return res





        '''
        res = [0] * len(nums)
        count = Counter(nums)
        if count[0] > 1:
            return res
            

        product = 1
        for i in nums:
            if i == 0:
                continue
            product *= i
        
        for idx, n in enumerate(nums):
            if count[0] == 0:
        '''
        


        
        