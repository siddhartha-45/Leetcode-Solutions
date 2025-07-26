class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=0
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
        return nums



        