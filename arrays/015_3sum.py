"""
001_two_sum.py
https://leetcode.com/problems/3sum/description/
#medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from arrays.utils import compare_lists_of_lists


def tree_sum(nums: list[int]) -> list[list[int]]:
    # bruteforce solution, O(n^3)
    result = []
    used_indexes = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if sum((nums[i], nums[j], nums[k])) == 0 and not {i, j, k}.issubset(
                    used_indexes
                ):
                    result.append([nums[i], nums[j], nums[k]])
                    used_indexes.update((i, j, k))

    return result


def tree_sum_hashmap(nums: list[int]) -> list[list[int]]:
    # hashmap solution, O(n^2)
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements

        left, right = i + 1, len(nums) - 1
        while left < right:
            triplet = [nums[i], nums[left], nums[right]]
            if s := sum(triplet) == 0:
                result.append(triplet)
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    result = tree_sum(nums=[-1, 0, 1, 2, -1, -4])
    assert compare_lists_of_lists(result, [[-1, -1, 2], [-1, 0, 1]]), result

    result = tree_sum(nums=[0, 1, 1])
    assert result == [], result

    result = tree_sum(nums=[0, 0, 0])
    assert result == [[0, 0, 0]], result
