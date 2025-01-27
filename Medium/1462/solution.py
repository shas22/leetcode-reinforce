from typing import List

class Solution:
    def checkIfPrerequisite(
        self, 
        n: int, 
        prerequisites: List[List[int]], 
        queries: List[List[int]]
    ) -> List[bool]:
        reachability = [[False] * n for _ in range(n)]

        for prerequisite, course in prerequisites:
            reachability[prerequisite][course] = True

        for intermediate_course in range(n):
            for start_course in range(n):
                for end_course in range(n):
                    if reachability[start_course][intermediate_course] and reachability[intermediate_course][end_course]:
                        reachability[start_course][end_course] = True

        
        result = []
        for query in queries:
            start_course, end_course = query
            result.append(reachability[start_course][end_course])

        return result