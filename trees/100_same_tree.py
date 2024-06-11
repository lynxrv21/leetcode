"""
100_same_tree.py
https://leetcode.com/problems/same-tree/description/
#easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

from trees.utils import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # recursive approach
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_same_tree1(p: TreeNode | None, q: TreeNode | None) -> bool:
    # iterative approach
    queue = [(p, q)]

    while queue:
        # p1, q1 = queue.pop(0)  # BFS way to traverse the tree
        p1, q1 = queue.pop()  # DFS way to traverse the tree
        if not p1 and not q1:
            continue
        if not p1 or not q1 or p1.val != q1.val:
            return False

        queue.append((p1.left, q1.left))
        queue.append((p1.right, q1.right))

    return True


if __name__ == "__main__":
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    result1 = is_same_tree1(p1, q1)
    assert result1 is True, result1

    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    result2 = is_same_tree1(p2, q2)
    assert result2 is False, result2

    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    result3 = is_same_tree1(p3, q3)
    assert result3 is False, result3
