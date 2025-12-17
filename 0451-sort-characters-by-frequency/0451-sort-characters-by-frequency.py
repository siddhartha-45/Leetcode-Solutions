class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        res=""
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        sorted_chars=sorted(freq, key=freq.get, reverse=True)
        for i in sorted_chars:
            res+=i*freq[i]
        return res