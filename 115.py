
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        dp = [0] * (m + 1)
        dp[0] = 1

        for ch in s:
            for j in range(m - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]

        return dp[m]
