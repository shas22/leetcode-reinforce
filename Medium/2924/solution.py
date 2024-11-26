class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        
        for _, target_node in edges:
            in_degree[target_node] += 1
        
        zero_in_degree_nodes = in_degree.count(0)
        
        if zero_in_degree_nodes == 1:
            return in_degree.index(0)
        else:
            return -1