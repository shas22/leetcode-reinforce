class PrefixSum:
    def __init__ (self, nums):
        self.prefix = []
        total = 0 
        for num in nums:
            total += nums
            self.prefix.append(total)

    def rangeFinder(self, left, right):
        self.right = self.prefix[right]
        self.left = self.prefix[left - 1] if left > 0 else 0
        return self.right - self.left





"""

Explanation:

input = [1, 2, 3, 4]

self.prefix = [1, 3, 6, 10]

The prefix i-th index gives you the total sum up until that point for example at self.prefix[3] is 6, that is the total sum of self.prefix[0] till self.prefix[3].

We can now use this to find subarray sums in o(N) time complexity.

Usage:

rangeFinder(1, 3)

This means we want to find the subarray sum of elements 1 through 3. Given that we have subarray sum up until 3 which is self.prefix[3] and we have the sum of self.prefix[0] (which is just a sum of itself), we can use self.prefix[3] - self.prefix[0]

"""