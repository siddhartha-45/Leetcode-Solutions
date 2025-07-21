class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        freq={}
        for i in range(n):
            freq[score[i]]=i
        score.sort(reverse=True)
        answer=[0]*n
        for i in range(n):
            if i==0:
                answer[freq[score[i]]]="Gold Medal"
            elif i==1:
                answer[freq[score[i]]]="Silver Medal"
            elif i==2:
                answer[freq[score[i]]]="Bronze Medal"
            else:
                answer[freq[score[i]]]=str(i+1)
        return answer