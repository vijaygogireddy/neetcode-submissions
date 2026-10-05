class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # c = Counter(nums)
        # return sorted(c, key=c.get, reverse=True)[:k]

        return [num for num, freq in Counter(nums).most_common(k)]

        
        # Counter Map
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        '''
        # O(n) - using extra space 10ms 27%
        n = len(nums)
        arr = [0] * (n + 1)

        for num, count in hashMap.items():
            if arr[count] == 0:
                arr[count] = [num]
                continue
            arr[count].append(num)

        res = []
        for i in range(n, -1, -1):
            if arr[i] != 0: 
                res.extend(arr[i])
            if len(res) == k:
                return res
        '''
            

        '''
        # O(nlogk) - using heap -> 3ms beats 90%
        heapArray = []
        for num, count in hashMap.items():
            if len(heapArray) < k:
                heapq.heappush(heapArray, (count, num))
                continue
            heapq.heappushpop(heapArray, (count, num))
        
        # [(3,1), (2,2)]
        return [heapArray[i][1] for i in range(k)]
        '''
        
        
        