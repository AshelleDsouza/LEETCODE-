class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if s[0] == mx and s[-1] == mn:
            if s.count(mn) > 1 or s.count(mx) > 1:
                return 2
            return 3
        return 2