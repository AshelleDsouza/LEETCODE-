class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        count = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                count[f] += freq[j]

        pmin = min(p for f, p in items)

        bonus = {}

        for f, p in items:
            d = count[f] - 1
            bonus[p] = bonus.get(p, 0) + d

        ans = 0

        for p in sorted(bonus):
            if p >= 2 * pmin:
                break

            take = min(bonus[p], budget // p)

            ans += 2 * take
            budget -= take * p

        ans += budget // pmin

        return ans