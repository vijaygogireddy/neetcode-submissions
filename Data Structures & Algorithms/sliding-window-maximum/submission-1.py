class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        res = []

        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap and heap[0][1] <= r - k:
                heapq.heappop(heap)

            if r >= k - 1:
                res.append(-heap[0][0])

        return res
        
        ''''''
        l=0
        res = []
        for r in range(k, len(nums)+1):
            res.append(max(nums[l : r]))
            l += 1
        
        return res