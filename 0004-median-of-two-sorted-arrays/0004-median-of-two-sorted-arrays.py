class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged_sort=sorted(merged)
        n=len(merged_sort)
        median=0
        mid=n//2
        if n%2==0:
            med_arr=merged_sort[mid-1]+merged_sort[mid]
            median=med_arr/2
            return median
        else:
            return merged_sort[mid]