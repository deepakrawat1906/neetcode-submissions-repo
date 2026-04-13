class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subArray = 1
            currSum = 0
            for num in nums:
                currSum+=num
                if currSum>largest:
                    subArray+=1
                    if subArray>k:
                        return False
                    currSum = num
            return True

        l = max(nums)
        r = sum(nums)
        res = 0
        while l<=r:
            m = (l+r)//2

            if canSplit(m):
                res = m
                r = m-1
            else:
                l=m+1
        return res
        