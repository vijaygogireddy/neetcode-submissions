class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n^2) Time | O(1) Space
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
                