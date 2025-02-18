class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,x in enumerate(nums):
            diff=target-x
            if diff in hashmap:
                val=hashmap[diff]
                return [val,i]
            hashmap[x]=i