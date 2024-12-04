class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for char in str1:
            if (ord(str2[i])-ord(char))%26 > 1:
                continue

            i += 1
            if i == len(str2):
                return True

        return False