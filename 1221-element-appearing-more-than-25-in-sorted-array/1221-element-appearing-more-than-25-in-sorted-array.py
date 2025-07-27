class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq={}
        n=len(arr)
        x=(n*25)/100
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,val in freq.items():
            if val>x:
                return k