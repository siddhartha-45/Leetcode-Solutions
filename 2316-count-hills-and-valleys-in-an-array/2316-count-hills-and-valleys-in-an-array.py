class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                arr.append(nums[i])
        count=0
        m=len(arr)
        for i in range(1,m-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                count+=1
            elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                count+=1
        return count
        