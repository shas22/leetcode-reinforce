class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = count = blocks[:k].count('W')

        for i in range(k, len(blocks)):
            count += blocks[i] == 'W'
            count -= blocks[i - k] == 'W'
            res = min(res, count)
            
        return res