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

