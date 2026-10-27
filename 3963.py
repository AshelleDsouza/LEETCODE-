class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                grid.append('.' * n)
            else:
                grid.append('#' * (n - 1) + '.')
        return grid