class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        if sentence[0] != sentence[len(sentence)-1]:
            return False

        for i in range(1, len(sentence)):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
                
        
        return True
