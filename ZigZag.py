def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        ans=['']*numRows
        ind = 0
        #print(ans}
        for k in range(len(s)):
            if ind==0:
                flag=True
            elif ind==numRows-1:
                flag=False
            if flag:
                ans[ind]+=s[k]
                ind+=1
            else:
                ans[ind] = ans[ind] + s[k]
                ind-=1
        answer=''
        for u in range(len(ans)):
            answer+=ans[u]
        return answer
