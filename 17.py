class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mp = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []
        path = []

        def backtrack(i):
            if i == len(digits):
                res.append(''.join(path))
                return
            for ch in mp[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res