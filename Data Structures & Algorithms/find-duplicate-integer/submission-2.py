class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Floyd's Tortoise and Hare Algorithm (Fast & Slow Pointers)
        # with given constraints
        # each array index as a node, and the value at that index as the pointer to the next node.
        # nums -> [1, n]
        slow = fast = nums[0]

        # find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # find cycle start point

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        
        
        # O(nlogn) time; modifying array
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]


        # O(n) space
        c = Counter(nums)
        return c.most_common()[0][0]