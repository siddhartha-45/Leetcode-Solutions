class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums=[]
        arr.sort()
        min_diff=float('inf')
        n=len(arr)
        for i in range(1,n):
            diff=(arr[i]-arr[i-1])
            if diff<min_diff:
                min_diff=diff
                nums=[[arr[i-1],arr[i]]]
            elif diff==min_diff:
                nums.append([arr[i-1],arr[i]])
        return nums