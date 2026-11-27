
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        groups = {}

        for i, (f, p) in enumerate(items):
            free = sum(1 for j, (g, _) in enumerate(items)
                       if i != j and g % f == 0)
            groups.setdefault(p, []).append(free + 1)

        dp = [-1] * (budget + 1)
        dp[0] = 0
        ans = 0

        for p in sorted(groups, reverse=True):
            cur = [-1] * (budget + 1)

            for v in groups[p]:
                for b in range(budget, p - 1, -1):
                    best = dp[b - p]
                    if cur[b - p] != -1:
                        best = max(best, cur[b - p])

                    if best != -1:
                        cur[b] = max(cur[b], best + v)

            for b in range(p, budget + 1):
                if cur[b] != -1:
                    extra = (budget - b) // p
                    ans = max(ans, cur[b] + extra)
                    dp[b] = max(dp[b], cur[b])

        return ans
