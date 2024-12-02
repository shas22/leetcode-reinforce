class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next(
            (index + 1 for index, word in enumerate(sentence.split()) 
             if word.startswith(searchWord)), 
            -1
        )