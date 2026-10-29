class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        # iterative DFS: Euler tour + parents
        it = [0] * n
        stack = [0]
        timer = 1
        while stack:
            u = stack[-1]
            if it[u] < len(adj[u]):
                v = adj[u][it[u]]
                it[u] += 1
                if v == up[0][u]:
                    continue
                up[0][v] = u
                depth[v] = depth[u] + 1
                tin[v] = timer
                timer += 1
                stack.append(v)
            else:
                tout[u] = timer  # exclusive end
                stack.pop()

        for k in range(1, LOG):
            pk, pp = up[k], up[k - 1]
            for v in range(n):
                pk[v] = pp[pp[v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff >> k & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def range_xor(l, r, x):  # [l, r)
            add(l, x)
            add(r, x)

        def point(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = list(s)
        for u in range(n):
            range_xor(tin[u], tout[u], 1 << (ord(chars[u]) - 97))

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                if chars[u] != c:
                    x = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                    range_xor(tin[u], tout[u], x)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = point(tin[u]) ^ point(tin[v]) ^ (1 << (ord(chars[w]) - 97))
                ans.append(mask & (mask - 1) == 0)
        return ans