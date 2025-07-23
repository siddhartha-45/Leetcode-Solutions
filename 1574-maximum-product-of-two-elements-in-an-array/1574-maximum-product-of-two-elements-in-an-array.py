class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        max_prod=0
        for i in range(0,n-1):
            for j in range(i+1,n):
                prod=(nums[i]-1)*(nums[j]-1)
                max_prod=max(prod,max_prod)
        return max_prod

            