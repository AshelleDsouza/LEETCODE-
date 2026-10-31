class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (R[i][j] + D[i][j]) % MOD

                if grid[i][j] == 0:
                    if i == m - 1 and j == n - 1:
                        return ways
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + ways) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + ways) % MOD
                else:
                    # mirror: right-arrivals bounce down, down-arrivals bounce right
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + R[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + D[i][j]) % MOD
        return 0