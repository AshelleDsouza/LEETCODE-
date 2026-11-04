class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        pos = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        LOG = m.bit_length()

        def update(i, dc, ds):
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(kk):
            p = 0
            for b in range(LOG, -1, -1):
                nxt = p + (1 << b)
                if nxt <= m and cnt[nxt] < kk:
                    p = nxt
                    kk -= cnt[nxt]
            return p + 1

        # cost[i] = ops to make nums[i:i+x] all equal
        W = n - x + 1
        cost = [0] * W
        total = 0
        for i in range(n):
            update(pos[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(pos[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                p = kth((x + 1) // 2)
                med = vals[p - 1]
                c, s = prefix(p)
                cost[i - x + 1] = (med * c - s) + ((total - s) - med * (x - c))

        INF = float('inf')
        prev = [0] * (n + 1)          # j = 0 windows: cost 0 everywhere
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x:
                    cand = prev[i - x] + cost[i - x]
                    if cand < cur[i]:
                        cur[i] = cand
            prev = cur

        return prev[n]