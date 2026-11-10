class Solution:
    def climbStairs(self, n: int) -> int:
        
        # DP
        dp = [0] * n

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]


        
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