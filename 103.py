from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []
        left = True

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level if left else level[::-1])
            left = not left

        return ans