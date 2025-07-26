class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        n=len(nums)
        res=[0]*n
        n=len(nums)
        while left<n and right<n:
            for i in nums:
                if i%2==0:
                    res[left]=i
                    left+=2
                elif i%2!=0:
                    res[right]=i
                    right+=2
        return res
