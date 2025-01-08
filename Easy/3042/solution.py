class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s: str, t: str) -> bool:
            if len(s) > len(t):
                return False
            return t[:len(s)] == s and t[-len(s):] == s
            
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count