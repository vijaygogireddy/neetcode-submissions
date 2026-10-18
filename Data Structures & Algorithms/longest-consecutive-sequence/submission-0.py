class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        
        hashSet = set(nums)

        for n in nums:
            if n-1 not in hashSet:
                k = n
                length = 0
                while k in hashSet:
                    length += 1
                    k+=1
                maxLength = max(length, maxLength)

        return maxLength
                



