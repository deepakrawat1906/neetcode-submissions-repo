class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        ans = 0
        d = {0:1}
        for num in nums:
            currSum+=num
            diff = currSum-k

            ans+=d.get(diff,0)
            d[currSum] = 1 + d.get(currSum,0)

        return ans
        