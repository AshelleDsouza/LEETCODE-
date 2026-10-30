class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lo, hi = min(strs), max(strs)
        i = 0
        while i < len(lo) and lo[i] == hi[i]:
            i += 1
        return lo[:i]