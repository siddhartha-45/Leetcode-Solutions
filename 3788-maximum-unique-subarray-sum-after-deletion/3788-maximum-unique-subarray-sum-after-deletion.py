class Solution:
    def maxSum(self, nums: List[int]) -> int:
        count_sum=0
        for i in set(nums):
            if i>0:
                count_sum+=i
        if count_sum==0:
            return max(nums)
        return count_sum
        