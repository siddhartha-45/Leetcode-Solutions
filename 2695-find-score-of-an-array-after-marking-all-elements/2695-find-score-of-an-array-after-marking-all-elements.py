class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = sorted([(n, i) for i, n in enumerate(nums)])
        marked = set()
        score = 0

        for n, i in nums:
            if i in marked:
                continue

            score += n
            marked.add(i)
            marked.add(i - 1)
            marked.add(i + 1)

        return score