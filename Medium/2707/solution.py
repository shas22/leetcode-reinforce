class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        word_set = set(dictionary)
        
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1 
            
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]