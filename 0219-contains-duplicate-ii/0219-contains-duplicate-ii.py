class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for i, val in enumerate(nums):
            if val in freq and i-freq[val]<=k:
                return True
            freq[val]=i
        return False