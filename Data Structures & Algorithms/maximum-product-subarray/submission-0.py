class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        n = len(nums)
        maxval = -100000

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *=nums[i]
            suffix*=nums[n-i-1]
            maxval = max(maxval,prefix,suffix)
        
        return maxval

        