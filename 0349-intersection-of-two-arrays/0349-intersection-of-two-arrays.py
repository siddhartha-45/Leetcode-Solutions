class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        arr1 = []
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                arr.append(nums1[i])
        for i in arr:
            if i not in arr1:
                arr1.append(i)
        return arr1