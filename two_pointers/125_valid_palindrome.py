"""
125_valid_palindrome.py
https://leetcode.com/problems/valid-palindrome/description/
#easy

Given a string s, return true if it is a palindrome, or false otherwise.

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
"""


def is_palindrome(s: str) -> bool:
    stripped = "".join(c.lower() for c in s if c.isalnum())

    if not stripped:
        return True

    p1, p2 = 0, len(stripped) - 1
    while p1 < p2:
        if stripped[p1] != stripped[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
