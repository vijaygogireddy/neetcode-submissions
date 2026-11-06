class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # O(n) space
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
                continue
            
            hashset.add(num)

        return list(hashset)