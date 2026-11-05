class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for i in range(1, 4):
                part = s[start:start + i]

                if len(part) != i:
                    continue

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                backtrack(start + i, path + [part])

        backtrack(0, [])
        return result