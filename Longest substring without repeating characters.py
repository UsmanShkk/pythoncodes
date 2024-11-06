def lengthOfLongestSubstring(self, s: str) -> int:
        tempr=[]
        maxr=0
        for i in range(len(s)):
            if tempr.count(s[i])==0:
                tempr.append(s[i])
            elif tempr.count(s[i])!=0:
                if len(tempr)>maxr:
                    maxr=len(tempr)
                while s[i] in tempr:
                    tempr.pop(0)
                tempr.append(s[i])
            if i==len(s)-1:
                if len(tempr)>maxr:
                    maxr=len(tempr)
        return(maxr)
