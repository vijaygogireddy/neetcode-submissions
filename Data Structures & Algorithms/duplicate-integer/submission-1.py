class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        count=0
        for num, freq in c.items():
            if freq > 1:
                count=1
        return True if count>0 else False
