class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):

            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i > 1:
                two = int(s[i - 2:i])

                if 10 <= two <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]