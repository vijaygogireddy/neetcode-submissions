class Solution:
    def reverse(self, x: int) -> int:
        
        # pre-check and use abs()
        sign = -1 if x<0 else 1
        x = abs(x)
        rev = 0

        # n = int(str(x)[::-1])

        # use arithmetic operation
        # 1234
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        n = sign * rev

        return n if -2**31 <= n < 2**31 else 0

        # using string conversion and indexing (slicing)
        s = str(x)[::-1]
        if s[-1] == "-":
            n = - int(s[:-1])
        else:
            n = int(s)

        return n if -2**31 <= n < 2**31 else 0