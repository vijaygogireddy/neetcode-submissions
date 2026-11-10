class Solution:
    def climbStairs(self, n: int) -> int:
        
        # DP

        
        # Memoization
        
        # Recursion with @cache
        def rec(n):
            if n == 1: return 1
            if n == 2: return 2

            one_rec = rec(n-1)
            two_rec = rec(n-2)

            return one_rec + two_rec
        
        return rec(n)

        
        # Fibonacci Logic
        a = b = 1

        for i in range(n-1):
            temp = a
            a = a + b
            b = temp

        return a