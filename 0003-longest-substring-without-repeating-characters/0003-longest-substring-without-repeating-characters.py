class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen=1
        curr_set=set()
        sub_str=""
        
        for char in s:
            if char not in curr_set:
                sub_str+=char
                curr_set.add(char)
            else:
                maxlen=max(maxlen,len(curr_set))
                sub_str+=char
                index=0
                while(sub_str[index]!=char):
                    index+=1
                
                sub_str=sub_str[index+1:]
                curr_set=set(sub_str)
        maxlen=max(maxlen,len(curr_set))

        return maxlen