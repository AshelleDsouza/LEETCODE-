class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []

        def backtrack(open_count, close_count):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res