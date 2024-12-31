class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
            n = days[-1]

            max_cost = max(costs) * n

            dp = [0] + [max_cost] * n

            price = {1:costs[0], 7:costs[1], 30:costs[2]}
            
            for i in range(1,len(dp)):
                if i not in days:
                    dp[i] = dp[i-1]
                    continue

                for ticket in [1, 7, 30]:
                    if i >= ticket:
                        dp[i] = min(dp[i],dp[i - ticket] + price[ticket])
                    else:
                        dp[i] = min(dp[i], dp[0] + price[ticket])

            return dp[-1]