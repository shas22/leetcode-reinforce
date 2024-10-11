class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        
        arr = [(times[i][0], i) for i in range(n)]
        
        arr.sort()
        
        availChairs = list(range(n))
        heapq.heapify(availChairs)

        leaving = []
        
        for arrivalTime, friendIndex in arr:
            while leaving and leaving[0][0] <= arrivalTime:
                heapq.heappush(availChairs, heapq.heappop(leaving)[1])
            
            chair = heapq.heappop(availChairs)
            
            if friendIndex == targetFriend:
                return chair
            
            heapq.heappush(leaving, (times[friendIndex][1], chair))
        
        return -1  