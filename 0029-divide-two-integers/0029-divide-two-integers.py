class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=int(dividend/divisor)
        INT_MAX=2**31- 1
        INT_MIN= -2**31
        if res>INT_MAX:
            return INT_MAX
        if res<INT_MIN:
            return INT_MIN
        return res