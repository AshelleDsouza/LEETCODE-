class Solution:
    def totalNQueens(self, n: int) -> int:
        full = (1 << n) - 1

        def solve(cols, diag, anti):
            if cols == full:
                return 1
            count = 0
            avail = ~(cols | diag | anti) & full
            while avail:
                bit = avail & -avail
                avail ^= bit
                count += solve(
                    cols | bit,
                    ((diag | bit) << 1) & full,
                    (anti | bit) >> 1,
                )
            return count

        return solve(0, 0, 0)