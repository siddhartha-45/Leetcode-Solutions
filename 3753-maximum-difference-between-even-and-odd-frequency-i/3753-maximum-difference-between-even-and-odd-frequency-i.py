class Solution:
    def maxDifference(self, s: str) -> int:
        even=len(s)
        odd=0
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key,val in freq.items():
                if val%2==0:
                    even=min(even,val)
                else:
                    odd=max(odd,val)
        return odd-even
                
            