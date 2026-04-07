class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prd = 1
        res = [1]*(len(nums))
        for i in range(len(nums)):
            res[i] = prefix_prd
            prefix_prd*=nums[i]

        postfix_prd = 1

        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix_prd
            postfix_prd*=nums[i]

        return res 
    

        