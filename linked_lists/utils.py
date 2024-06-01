# helper function for linked lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


def get_list_values(node: ListNode) -> list:
    """Get the list of nodes values"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def create_linked_list(values: list[int]) -> ListNode:
    prev = None
    while values:
        new_node = ListNode(values.pop(), next=prev)
        prev = new_node
    return new_node
