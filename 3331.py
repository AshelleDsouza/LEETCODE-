
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        stack = [(0, False, -1)]

        while stack:
            node, exit, old = stack.pop()
            ch = s[node]

            if exit:
                if old == -1:
                    last.pop(ch, None)
                else:
                    last[ch] = old
                continue

            old = last.get(ch, -1)

            if node != 0 and old != -1:
                new_parent[node] = old

            last[ch] = node
            stack.append((node, True, old))

            for child in reversed(children[node]):
                stack.append((child, False, -1))

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = [0]
        stack = [0]

        while stack:
            node = stack.pop()
            for child in new_children[node]:
                order.append(child)
                stack.append(child)

        ans = [1] * n

        for node in reversed(order[1:]):
            ans[new_parent[node]] += ans[node]

        return ans
