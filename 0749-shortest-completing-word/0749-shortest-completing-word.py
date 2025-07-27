class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        s=[]
        licensePlate=licensePlate.lower()
        for i in licensePlate:
            if i.isalpha():
                s.append(i)
        words=sorted(words, key=len)
        for word in words:
            temp=list(word.lower())
            flag=True
            for i in s:
                if i in temp:
                    temp.remove(i)
                else:
                    flag=False
                    break
            if flag:
                return word