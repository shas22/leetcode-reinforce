class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        n = len(graph)
        safe = {}


        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False

            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return safe[i]

            safe[i] = True
            return safe[i]

        for i in range(len(graph)):
            if dfs(i): res.append(i)

        return res