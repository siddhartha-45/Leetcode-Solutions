class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = s.lower()
        n = ''.join(filter(str.isalnum, m))
        return n == n[::-1]