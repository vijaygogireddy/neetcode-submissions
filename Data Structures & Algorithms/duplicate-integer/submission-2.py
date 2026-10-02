class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        # c= {1: 1, 2: 1, 3: 2, 4:1}

        flag=0
        for num, freq in c.items():
            if freq > 1:
                flag=1
                return True
        return False
