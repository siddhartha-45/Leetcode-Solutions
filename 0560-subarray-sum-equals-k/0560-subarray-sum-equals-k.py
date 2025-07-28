class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum=0
        freq={}
        n=len(nums)
        for i in range(n):
            prefix_sum+=nums[i]
            if prefix_sum==k:
                count+=1
            if (prefix_sum-k) in freq:
                count+=freq[prefix_sum-k]
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count