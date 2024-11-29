class Solution:
    def permute(self, nums):
        def backtrack(current_perm, remaining):

            if not remaining:
                result.append(current_perm[:])
                return
            
            for i in range(len(remaining)):
                current_perm.append(remaining[i])
                
                backtrack(current_perm, remaining[:i] + remaining[i+1:])

                current_perm.pop()
        
        result = []
        backtrack([], nums)
        return result
