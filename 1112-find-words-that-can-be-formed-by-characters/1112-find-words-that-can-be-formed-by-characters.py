from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char=Counter(chars)
        count=0
        for word in words:
            if Counter(word)<=char:
                count+=len(word)
        return count