class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = None

        for i in range(m):
            cur = []
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    s = {v}
                else:
                    src = set()
                    if i > 0:
                        src |= prev[j]
                    if j > 0:
                        src |= cur[j - 1]
                    s = {x ^ v for x in src}
                cur.append(s)
            prev = cur

        return min(prev[-1])