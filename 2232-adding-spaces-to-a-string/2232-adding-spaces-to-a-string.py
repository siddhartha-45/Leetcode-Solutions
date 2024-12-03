class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=[]
        idx=0
        for i in spaces:
            result.append(s[idx:i])
            result.append(" ")
            idx=i  
        result.append(s[idx:])  
        return "".join(result)