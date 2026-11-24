
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path[:])
            else:
                dfs(node.left, path, total)
                dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)
        return ans
