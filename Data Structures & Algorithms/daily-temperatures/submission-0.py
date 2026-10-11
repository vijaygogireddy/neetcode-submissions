class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                pop_i, pop_n = stack.pop()
                res[pop_i] = i - pop_i
            
            stack.append((i, n))

        return res