class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1=Counter(magazine)
        str2=Counter(ransomNote)
        if str1&str2==str2:
            return True
        
        return False