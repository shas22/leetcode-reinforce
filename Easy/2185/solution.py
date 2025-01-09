class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        
        for word in words:
            prefix = True

            for i in range(len(pref)):
                if i >= len(word) or word[i] != pref[i]:
                    prefix = False
                    break

            if prefix:
                count += 1

        return count