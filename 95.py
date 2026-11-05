class Solution:
    def generateTrees(self, n):
        def build(start, end):
            if start > end:
                return [None]

            result = []

            for i in range(start, end + 1):
                left = build(start, i - 1)
                right = build(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        result.append(root)

            return result

        return build(1, n)