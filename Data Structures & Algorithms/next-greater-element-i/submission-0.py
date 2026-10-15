class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        hashMap = {v : i for i, v in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            val = nums2[i]

            while stack and val > stack[-1]:
                idx = hashMap[stack.pop()]
                res[idx] = val


            if val in hashMap:
                stack.append(val)

        return res
            
            
        