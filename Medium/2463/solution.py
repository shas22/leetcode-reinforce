class Solution(object):
    def minimumTotalDistance(self, robot, factory):

        robot.sort(), factory.sort()

        dp = [float("inf")]*(len(robot)+1)  
        
        dp[0] = 0

        for i in range(len(factory)):
            for j in reversed(range(1, len(robot)+1)):

                curr = 0

                for k in range(min(factory[i][1], j)+1):

                    dp[j] = min(dp[j], dp[j-k]+curr)

                    if (j-1)-k >= 0:
                        curr += abs(robot[(j-1)-k]-factory[i][0])

        return dp[-1]