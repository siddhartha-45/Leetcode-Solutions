class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        total=0
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,v in freq.items():
            if v==1:
                total+=k
        return total


        