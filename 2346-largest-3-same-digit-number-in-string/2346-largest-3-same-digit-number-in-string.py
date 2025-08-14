class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        arr=[]
        for i in range(2,n):
            if num[i]==num[i-1]==num[i-2]:
                arr.append(num[i-2:i+1])
        return max(arr) if arr else ""