import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        INF = float('inf')
        dist = [INF] * (n * K)
        min_run = [K] * n  # smallest run already settled at each node

        dist[0 * K + 1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, u, r = heapq.heappop(heap)
            if d > dist[u * K + r]:
                continue
            if r >= min_run[u]:
                continue
            min_run[u] = r
            if u == n - 1:
                return d
            for v, w in adj[u]:
                nr = r + 1 if labels[u] == labels[v] else 1
                if nr > k:
                    continue
                nd = d + w
                idx = v * K + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, v, nr))

        return 