from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertBinaryTree(tree: TreeNode):
    if not tree:
        return None

    tmp = tree.left
    tree.left = tree.right
    tree.right = tmp

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


class Solution:
    length = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            return max(self.length, dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)