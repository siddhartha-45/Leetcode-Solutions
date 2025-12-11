class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        freq={}
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for k,v in freq.items():
            if v>(n//3):
                res.append(k)
        return res