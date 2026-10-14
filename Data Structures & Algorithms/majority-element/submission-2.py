class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(n) time | O(1) space
        count = 0
        val = nums[0]
        for i in nums:
            if count == 0:
                val = i
            
            if i == val:
                count += 1
            else:
                count -= 1

        return val
            



        # O(nlogn) time | O(n) auxiliary space
        nums.sort()
        n = len(nums)
        return nums[n//2]