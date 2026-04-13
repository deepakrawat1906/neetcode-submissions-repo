class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r],0)
            #improvement
            maxf = max(maxf,countMap[s[r]])
            while (r-l) - maxf >=k:
                countMap[s[l]]-=1
                l+=1

            res = max(res,r-l+1)
        
        return res
        