class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str=list(str(num))
        n=len(num_str)
        for i in range(n):
            if num_str[i]=='6':
                num_str[i]='9'
                break
            
        return int("".join(num_str))