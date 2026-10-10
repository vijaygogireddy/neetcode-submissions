class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(str(bin(n)[2:]))
        return c.get('1', 0)