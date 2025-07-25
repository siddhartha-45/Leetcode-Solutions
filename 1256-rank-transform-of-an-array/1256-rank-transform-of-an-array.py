class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        freq={}
        sorted_set=sorted(list(set(arr))) 
        for i in range(len(sorted_set)): 
            freq[sorted_set[i]]=i+1
        for r in range(len(arr)): 
            arr[r]=freq[arr[r]]
        return arr