import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)
        for i in range(k):
            tree[size+i] = 1
        for i in range(size-1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]

        def update(i, val):
            i += size
            tree[i] = val
            while i > 1:
                i //= 2
                tree[i] = tree[2*i] + tree[2*i+1]

        def find(node, l, r, start):
            if r <= start or tree[node] == 0:
                return -1
            if l == r-1:
                return l
            mid = (l+r)//2
            a = find(2*node, l, mid, start)
            return a if a != -1 else find(2*node+1, mid, r, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, s = heapq.heappop(busy)
                update(s, 1)

            s = find(1, 0, size, i % k)
            if s == -1:
                s = find(1, 0, size, 0)

            if s != -1 and s < k:
                update(s, 0)
                count[s] += 1
                heapq.heappush(busy, (arrival[i]+load[i], s))

        m = max(count)
        return [i for i in range(k) if count[i] == m]