def normalize_list_of_lists(lst: list[list]) -> list[list]:
    # Sort each sublist
    normalized_lst = [sorted(sublist) for sublist in lst]
    # Sort the list of sorted sublists
    normalized_lst.sort()
    return normalized_lst


def compare_lists_of_lists(lst1: list[list], lst2: list[list]) -> bool:
    return normalize_list_of_lists(lst1) == normalize_list_of_lists(lst2)
