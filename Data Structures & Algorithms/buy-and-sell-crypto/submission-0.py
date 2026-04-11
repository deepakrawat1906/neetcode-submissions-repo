class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minVal = prices[0]

        for sell in prices:
            ans = max(ans,sell-minVal)
            minVal = min(minVal,sell)
        return ans

        