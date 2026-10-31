class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << int(board[r][c])
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def solve(remaining):
            if not remaining:
                return True

            # choose the empty cell with the fewest candidates
            best_idx, best_mask, best_count = -1, 0, 10
            for idx, (r, c) in enumerate(remaining):
                used = rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]
                avail = ~used & 0b1111111110      # bits 1..9 not used
                cnt = bin(avail).count('1')
                if cnt < best_count:
                    best_idx, best_mask, best_count = idx, avail, cnt
                    if cnt == 0:
                        return False
                    if cnt == 1:
                        break

            r, c = remaining[best_idx]
            b = (r // 3) * 3 + c // 3
            rest = remaining[:best_idx] + remaining[best_idx + 1:]

            mask = best_mask
            while mask:
                bit = mask & -mask               # lowest set bit
                mask ^= bit
                d = bit.bit_length() - 1

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(d)

                if solve(rest):
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'

            return False

        solve(empties)