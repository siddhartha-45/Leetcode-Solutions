class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            if nums[i]==target:
                res.append(i)
        if not res:
            return [-1,-1]
        return res[0],res[-1]
        