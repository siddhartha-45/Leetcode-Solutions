class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2)>len(str1):
            return False
        j=0
        n=len(str2)
        for i in str1:
            if j<n and (ord(str2[j])-ord(i))%26<2:
                j+=1
        if j==n:
            return True
        return False