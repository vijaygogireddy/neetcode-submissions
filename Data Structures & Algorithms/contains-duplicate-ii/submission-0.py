class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # abs(i - j) <= k

        # store num as key, idx as value in hashmap
        hashmap = {}

        for idx, num in enumerate(nums):
            if num in hashmap:
                return abs(idx - hashmap[num]) <= k

            hashmap[num] = idx

        return False