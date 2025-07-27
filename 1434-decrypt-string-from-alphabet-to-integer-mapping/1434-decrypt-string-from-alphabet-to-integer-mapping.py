class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=""
        st=0
        while st<len(s):
            if st+2<len(s) and s[st+2]=="#":
                num=int(s[st:st+2])
                res+=chr(num+96)
                st+=3
            else:
                num=int(s[st])
                res+=chr(num+96)
                st+=1
        return res