class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return "j"+(n-1)*"s"
        else:
            return "j"*n