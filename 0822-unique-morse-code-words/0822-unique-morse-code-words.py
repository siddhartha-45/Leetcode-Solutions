class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha_morse={
 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
 'y': '-.--', 'z': '--..'
}
        word_dup=[]
        for i in words:
            ss=""
            for j in range(len(i)):
                ss=ss+alpha_morse[i[j]]
            else:
                if ss not in word_dup:
                    word_dup.append(ss)
        return len(word_dup)


        


        