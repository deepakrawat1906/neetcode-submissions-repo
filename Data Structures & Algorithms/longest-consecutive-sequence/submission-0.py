class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapStore = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in mapStore:
                length=1
                while (num + length) in mapStore:
                    length+=1
                
                ans = max(ans,length)
        
        return ans
        