class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        # O(1) space
        a, b = 0, 0
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        # Extract rightmost set bit with 2's complement
        set_bit = xor & -xor

        for num in nums:
            if set_bit & num:
                a = a ^ num
            else:
                b = b ^ num
        
        return [a,b]

        
        # O(n) space
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
                continue
            
            hashset.add(num)

        return list(hashset)