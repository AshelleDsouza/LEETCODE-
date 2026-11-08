class Solution:
    def countServers(self, grid):
        rows = [sum(r) for r in grid]
        cols = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]

        return sum(1 for i in range(len(grid)) for j in range(len(grid[0]))
                   if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1))