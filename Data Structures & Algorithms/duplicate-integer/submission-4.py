class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # c = Counter(nums)
        # c= {1: 1, 2: 1, 3: 2, 4:1}
        c = {}
        for i in nums:
            c[i] = 1 + c.get(i, 0)

        flag=0
        for num, freq in c.items():
            if freq > 1:
                flag=1
                return True
        return False
        
        # using set to remove duplicates
        numSet = set(nums)
        return True if len(numSet) != len(nums) else False


        # O(n^2) Time | O(1) Space
        # TLE
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        