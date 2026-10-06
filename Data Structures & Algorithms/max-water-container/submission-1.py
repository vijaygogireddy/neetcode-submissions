class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # O(n)
        maxArea = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            maxArea = max(maxArea, area)
            
            
            if heights[l] < heights[r]:
                l += 1
                continue
            r -= 1
        
        return maxArea



        '''
        # Brute Force - O(n^2) - TLE
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                area = height * width
                maxArea = max(maxArea, area)
        return maxArea
        '''