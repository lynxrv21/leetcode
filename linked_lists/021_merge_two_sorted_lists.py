"""
021_merge_two_sorted_lists.py
https://leetcode.com/problems/merge-two-sorted-lists/description/
#easy

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""

from linked_lists.utils import ListNode, create_linked_list, get_list_values


def merge_two_lists(list1: ListNode|None, list2: ListNode|None) -> ListNode|None:
    dummy = ListNode(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next


if __name__ == "__main__":
    merged_list = merge_two_lists(
        create_linked_list([1, 2, 4]), create_linked_list([1, 3, 5])
    )
    result = get_list_values(merged_list)
    assert result == [1, 1, 2, 3, 4, 5], result

    merged_list = merge_two_lists(None, ListNode(0))
    result = get_list_values(merged_list)
    assert result == [0], result

    merged_list = merge_two_lists(None, None)
    result = get_list_values(merged_list)
    assert result == [], result
