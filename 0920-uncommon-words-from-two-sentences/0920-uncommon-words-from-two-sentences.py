class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq={}
        words=s1.split()+s2.split()
        for i in words:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res=[]
        for i in freq:
            if freq[i]==1:
                res.append(i)
        return res