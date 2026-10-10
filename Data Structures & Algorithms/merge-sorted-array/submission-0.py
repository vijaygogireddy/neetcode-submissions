class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i, k = i-1, k-1
                continue
            nums1[k] = nums2[j]
            j, k = j-1, k-1

        # for k in range(m+n-1, -1, -1):









        '''
        x = m - 1
        y = n - 1
        z = m + n - 1
        
        while y >= 0:
            if x >= 0 and nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
            z -= 1
        '''