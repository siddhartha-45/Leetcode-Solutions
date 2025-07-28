class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=nums.count(0)
        arr=[]
        for i in nums:
            if i!=0:
                arr.append(i)
        arr+=[0]*x
        for i in range(len(nums)):
            nums[i]=arr[i]