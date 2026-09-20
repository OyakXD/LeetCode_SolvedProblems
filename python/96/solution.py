class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n+1)
        dp[0] = 1

        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left = dp[root - 1]
                right = dp[nodes - root]
                dp[nodes] += left * right
        
        return dp[n]