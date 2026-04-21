class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        if len(s)==1:
            return s

        for i in range(len(s)):
            l = i
            r = i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = l
                    resLen = r-l+1
                l-=1
                r+=1

            l=i
            r=i+1 
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resLen:
                    res = l
                    resLen = r-l+1
                l-=1
                r+=1
        return s[res:res+resLen]
        