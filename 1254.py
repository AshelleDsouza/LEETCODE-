class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def fill(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        # remove land connected to the border
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and grid[i][j] == 0:
                    fill(i, j)

        # count remaining islands
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    fill(i, j)
        return count