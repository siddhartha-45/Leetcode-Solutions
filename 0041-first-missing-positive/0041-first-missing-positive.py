class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        temp=1
        for i in nums:
            if i==temp:
                temp+=1
        return temp