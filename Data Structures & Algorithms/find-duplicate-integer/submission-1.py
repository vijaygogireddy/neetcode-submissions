class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # O(nlogn) time; modifying array
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]


        # O(n) space
        c = Counter(nums)
        return c.most_common()[0][0]