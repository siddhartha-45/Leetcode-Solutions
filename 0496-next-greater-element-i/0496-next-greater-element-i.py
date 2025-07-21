class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater= {}

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        for num in stack:
            greater[num] = -1

        return [greater[num] for num in nums1]