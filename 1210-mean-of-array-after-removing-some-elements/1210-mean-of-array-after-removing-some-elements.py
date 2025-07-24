class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        m=int((n*5)/100)
        arr.sort()
        arr1=arr[m:n-m]
        k=len(arr1)
        return sum(arr1)/k