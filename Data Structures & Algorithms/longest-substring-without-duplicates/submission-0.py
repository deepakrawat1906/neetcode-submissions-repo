class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        index = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in d:
                index = max(d[s[i]]+1,index)

            ans = max(ans,i-index+1)
            d[s[i]] = i
        return ans
        