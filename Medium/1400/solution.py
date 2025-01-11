class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
      if len(s) <= k:
        return len(s) == k
      
      letters = {}

      for char in s:
        letters[char] = letters.get(char, 0) + 1
      
      count = sum(value % 2 for value in letters.values())
        
      return count <= k