class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        num = int(str(x)[::-1])

        return sign * num if -2**31 < num < 2**31 else 0