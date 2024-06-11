"""
104_maximum_depth_of_binary_tree.py
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.
"""

from trees.utils import TreeNode


def max_depth(root: TreeNode | None) -> int:
    if root:
        return 1 + max(max_depth(root.left), max_depth(root.right))
    else:
        return 0


if __name__ == "__main__":
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(r1) == 3, r1

    r2 = TreeNode(1, None, TreeNode(2))
    assert max_depth(r2) == 2, r2
