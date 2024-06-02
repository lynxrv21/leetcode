"""
242_valid_anagram.py
https://leetcode.com/problems/valid-anagram/description/
#easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


if __name__ == "__main__":
    result = is_anagram(s="anagram", t="nagaram")
    assert result is True, result

    result = is_anagram(s="rat", t="car")
    assert result is False, result
