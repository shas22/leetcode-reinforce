class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)

        while True:
            if s.find(part) != -1:
                index = s.find(part)
                s = s[0:index] + s[index + n:]
            else:
                break
                
        return s