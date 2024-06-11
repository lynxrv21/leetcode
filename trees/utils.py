# helper function for binary trees


class TreeNode:
    """Definition for a binary tree node."""

    def __repr__(self):
        return f"{self.val}: [{self.left}, {self.right}]"

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_tree_values(node: TreeNode) -> list:
    result = []
    queue = [node]

    while queue:
        n = queue[0]
        queue = queue[1:]
        result.append(n.val)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

    return result
