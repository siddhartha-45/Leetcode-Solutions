class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        n=len(startTime)
        for i in range(n):
            if startTime[i]<=queryTime<=endTime[i]:
                count+=1
        return count