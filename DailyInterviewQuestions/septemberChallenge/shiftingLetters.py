class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        def shift(letter,shift):
            if(ord(letter) + shift >= 122):
                return chr(97 + ((ord(letter) + shift - 97) % 26))
            else:
                return chr(ord(letter) + shift)
                           
        for i in range(len(shifts)-2,-1,-1):
            shifts[i] = shifts[i+1] + shifts[i]
            
        let = [e for e in s]
        for i in range(len(let)):
            let[i] = shift(let[i],shifts[i])
            
        return ''.join(let)
