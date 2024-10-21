class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, t, vis):
            if i >= len(s):
                return t
            
            max_splits = t
            for j in range(i + 1, len(s) + 1):
                if s[i:j] not in vis:
                    vis.add(s[i:j])
                    max_splits = max(max_splits, dfs(j, t+1, vis))
                    vis.remove(s[i:j])
            
            return max_splits

        return dfs(0, 0, set())