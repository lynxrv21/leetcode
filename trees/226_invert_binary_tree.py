"""
226_invert_binary_tree.py
https://leetcode.com/problems/invert-binary-tree/description/
#easy

Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional

from trees.utils import TreeNode, get_tree_values


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root


if __name__ == "__main__":
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    result = invert_tree(r1)
    assert get_tree_values(result) == [2, 3, 1], result

    r2 = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    result = invert_tree(r2)
    assert get_tree_values(result) == [4, 7, 2, 9, 6, 3, 1], result
