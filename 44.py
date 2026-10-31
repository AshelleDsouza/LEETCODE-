class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1   # index of the last '*' in p
        mark = 0    # index in s where that star's match currently ends

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                mark = i
                j += 1
            elif star != -1:
                mark += 1
                i = mark
                j = star + 1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)