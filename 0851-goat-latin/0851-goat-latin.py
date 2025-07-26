class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr=sentence.split(" ")
        fre="aeiouAEIOU"
        arrr=[]
        for i,word in enumerate(arr):
            if word[0] in fre:
                word+="ma"
            else:
                word=word[1:]+word[0]+"ma"
            word+="a"*(i+1)
            arrr.append(word)
        return " ".join(arrr)