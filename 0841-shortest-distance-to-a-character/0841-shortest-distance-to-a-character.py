class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        res=[float('inf')] * n
        prev=-float('inf')
        for i in range(n):
            if s[i]==c:
                prev=i
            res[i]=abs(i-prev)
        prev=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
                prev=i
            res[i]=min(res[i],abs(i-prev))
        return res