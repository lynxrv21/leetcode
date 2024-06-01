"""
206_reverse_linked_list.py
https://leetcode.com/problems/reverse-linked-list/description/
#easy

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from linked_lists.utils import ListNode, create_linked_list, get_list_values


def reverse_list(head: ListNode | None) -> ListNode:

    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def reverse_list_recursive(self, head: ListNode) -> ListNode:
    if head and head.next:
        newhead = self.reverseList(head.next)
        head.next.next, head.next = head, None
        head = newhead
    return head


if __name__ == "__main__":
    reversed_list = reverse_list(create_linked_list([1, 2, 3, 4, 5]))
    result = get_list_values(reversed_list)
    assert result == [5, 4, 3, 2, 1], result

    reversed_list = reverse_list(create_linked_list([1, 2]))
    result = get_list_values(reversed_list)
    assert result == [2, 1], result
