"""
141_linked_list_cycle.py
https://leetcode.com/problems/linked-list-cycle/description/
#easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index
of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from linked_lists.utils import ListNode, create_linked_list


def has_cycle(head: ListNode | None) -> bool:
    nodes_hash = set()

    while head:
        if head in nodes_hash:
            return True
        nodes_hash.add(head)
        head = head.next

    return False


def has_cycle_two_pointer(head: ListNode | None) -> bool:
    slow_p, fast_p = head, head

    while fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if slow_p == fast_p:
            return True

    return False


if __name__ == "__main__":
    list1_head = create_linked_list([3, 2, 0, -4])
    pos = list1_head.next
    pos.next.next.next = pos
    result = has_cycle(list1_head)
    assert result is True, result

    list2_head = create_linked_list([3, 2])
    list2_head.next.next = list2_head

    result = has_cycle(list2_head)
    assert result is True, result

    result = has_cycle(ListNode(1))
    assert result is False, result
