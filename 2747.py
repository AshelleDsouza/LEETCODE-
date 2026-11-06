class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))

        count = {}
        ans = [0] * len(queries)
        l = r = 0

        for t, i in q:
            while r < len(logs) and logs[r][1] <= t:
                s = logs[r][0]
                count[s] = count.get(s, 0) + 1
                r += 1

            while l < r and logs[l][1] < t - x:
                s = logs[l][0]
                count[s] -= 1
                if count[s] == 0:
                    del count[s]
                l += 1

            ans[i] = n - len(count)

        return ans