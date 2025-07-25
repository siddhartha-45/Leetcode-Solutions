class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid=n//2
        arr=[]
        for i in range(1,mid+1):
            arr.append(-i)
            arr.append(i)
        if n%2!=0:
            arr.append(0)
        return arr

