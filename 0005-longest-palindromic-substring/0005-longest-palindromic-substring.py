class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = len(s)
        while k > 0:
            for i in range(len(s)-k+1):
                if s[i:i+k] == s[i:i+k][::-1]:
                    return s[i:i+k]
            k -= 1
        return ""