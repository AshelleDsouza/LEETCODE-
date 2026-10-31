class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                c = candidates[i]
                if c > remaining:
                    break
                path.append(c)
                backtrack(i + 1, remaining - c)
                path.pop()

        backtrack(0, target)
        return res