class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
    
        res = len(nums)+1

        l = 0
        curr = 0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                res = min(res,r-l+1)
                curr-=nums[l]
                l+=1
        
        return 0 if res==len(nums)+1 else res

        

        