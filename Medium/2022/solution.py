class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []  
        
    
        reshaped_matrix = []
        for i in range(0, m * n, n):
            row = original[i : i + n]
            
            reshaped_matrix.append(row)
        
        return reshaped_matrix