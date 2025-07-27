class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq={}
        res=[]
        nums1=sorted(nums)
        n=len(nums1)
        for i in range(0,n):
            num=nums1[i]
            if nums1[i] not in freq:
                freq[num]=i
        for num in nums:
            res.append(freq[num])
        return res
            