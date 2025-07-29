class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_arr=[]
        t_arr=[]
        if len(s)!=len(t):
            return False
        for i in s:
            s_arr.append(s.index(i))
        for j in t:
            t_arr.append(t.index(j))
        if s_arr==t_arr:
            return True
        return False