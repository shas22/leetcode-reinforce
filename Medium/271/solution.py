class Solution:
    # end of string shall be `
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(0, len(strs)):
            encoded += strs[i] + "`"
            
        #words = who`
        #sentences = we are the smth`
            
            
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        for letter in s:
            if letter == "`":
                strs.append(word)
                word = ""
            else:
                word += letter
        return strs