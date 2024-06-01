"""
linked_lists/002_add_two_numbers.py
https://leetcode.com/problems/add-two-numbers/description/
#medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from linked_lists.utils import create_linked_list, get_list_values, ListNode


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(None)
    carry = 0

    curr = dummy

    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        summary = v1 + v2 + carry
        val, carry = summary % 10, summary // 10
        new = ListNode(val)

        curr.next = new
        curr = new
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry != 0:
        curr.next = ListNode(val=carry)

    return dummy.next


if __name__ == "__main__":
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    result = get_list_values(add_two_numbers(l1, l2))
    assert result == [7,0,8], result

    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    result = get_list_values(add_two_numbers(l1, l2))
    assert result == [8,9,9,9,0,0,0,1], result
