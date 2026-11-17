class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                best = float('inf')

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for x in range(d):
                            group = list(range(l + x, r + 1, d))

                            i, j = 0, len(group) - 1
                            while i < j:
                                if s[group[i]] != s[group[j]]:
                                    changes += 1
                                i += 1
                                j -= 1

                        best = min(best, changes)

                cost[l][r] = best

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]