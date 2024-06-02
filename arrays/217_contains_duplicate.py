"""
217_contains_duplicate.py
https://leetcode.com/problems/contains-duplicate/description/
#easy

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


def contains_duplicate(nums: list[int]) -> bool:
    # Hash set. The time complexity is O(n)
    n_set = set()

    for n in nums:
        if n in n_set:
            return True
        n_set.add(n)
    return False


if __name__ == "__main__":
    result = contains_duplicate([1, 2, 3, 1])
    assert result is True, result

    result = contains_duplicate([1, 2, 3, 4])
    assert result is False, result

    result = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert result is True, result
