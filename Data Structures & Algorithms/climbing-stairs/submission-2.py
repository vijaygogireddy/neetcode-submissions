class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Bottom-Up DP

        
        # Memoization
        memo = {}

        def rec(n):
            if n in memo: return memo[n]

            if n <= 2: return n

            res = rec(n-1) + rec(n-2)
            memo[n] = res

            return res
        
        return rec(n)

        
        # Fibonacci Logic
        a = b = 1

        for i in range(n-1):
            temp = a
            a = a + b
            b = temp

        return a