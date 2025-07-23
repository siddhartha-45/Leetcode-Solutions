class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        n=len(arr)
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        val=list(freq.values())
        if len(val)==len(set(val)):
            return True
        return False