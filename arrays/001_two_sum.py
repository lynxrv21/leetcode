"""
001_two_sum.py
https://leetcode.com/problems/two-sum/description/
#easy

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # bruteforce solution, O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    # hashmap solution, O(n)
    hash_table = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_table:
            return [i, hash_table[diff]]

        hash_table[num] = i


if __name__ == "__main__":
    result = two_sum(nums=[2, 7, 11, 15], target=9)
    assert result == [0, 1], result

    result = two_sum(nums=[3, 2, 4], target=6)
    assert result == [1, 2], result

    result = two_sum_hashmap(nums=[3, 2, 4], target=6)
    assert result == [1, 2], result
