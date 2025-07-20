class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        arr=[]
        for i in range(0,n,k):
            txt=s[i:i+k]
            if len(txt)<k:
                txt+=fill*(k-len(txt))
            arr.append(txt)
        return arr