class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for j in word2:
            s2+=j
        if s1==s2:
            return True
        return False