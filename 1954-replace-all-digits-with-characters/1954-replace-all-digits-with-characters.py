class Solution:
    def replaceDigits(self, s: str) -> str:
        res=[]
        for i in range(len(s)):
            if i%2==0:
                res.append(s[i])  
            else:
                shift=int(s[i])
                new_char=chr(ord(s[i-1])+shift)
                res.append(new_char)
        return ''.join(res)
