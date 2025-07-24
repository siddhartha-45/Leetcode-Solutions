class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        result=[""] * len(words)    
        for i in words:
            pos=int(i[-1])-1 
            actual_word=i[:-1]
            result[pos]=actual_word
        return " ".join(result)
        