class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def solve(a, b):
            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):
                if (solve(a[:i], b[:i]) and
                    solve(a[i:], b[i:])):
                    return True

                if (solve(a[:i], b[n-i:]) and
                    solve(a[i:], b[:n-i])):
                    return True

            return False

        return solve(s1, s2)