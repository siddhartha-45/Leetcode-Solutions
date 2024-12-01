class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return 1 + time
        res = time // (n - 1)
        rem = time % (n - 1)
        return 1 + rem if res % 2 == 0 else n - rem