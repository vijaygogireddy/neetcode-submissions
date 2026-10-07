class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):

            first = nums[i]

            if first > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if first + nums[i + 1] + nums[i + 2] > 0:
                break
            
            if first + nums[n - 1] + nums[n - 2] < 0:
                continue

            

            l, r =  i+1, n-1

            while l < r:
                add = nums[i] + nums[l] + nums[r]
                if add == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif add < 0:
                    l += 1
                else:
                    r -= 1

        return res