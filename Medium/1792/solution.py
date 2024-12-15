import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        heap = []
        
        for passed, total in classes:
            improvement = self.calculate_improvement(passed, total)
            heapq.heappush(heap, (-improvement, passed, total))
        
        for _ in range(extraStudents):
            _, passed, total = heapq.heappop(heap)

            new_passed, new_total = passed + 1, total + 1

            new_improvement = self.calculate_improvement(new_passed, new_total)
            heapq.heappush(heap, (-new_improvement, new_passed, new_total))

        return sum(passed / total for _, passed, total in heap) / len(classes)
    
    def calculate_improvement(self, passed, total):
        return (passed + 1) / (total + 1) - passed / total