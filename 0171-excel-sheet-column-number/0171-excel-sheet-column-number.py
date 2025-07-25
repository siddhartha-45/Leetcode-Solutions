class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total=0
        for i in columnTitle:
            total=total*26+(ord(i)-64)
        return total