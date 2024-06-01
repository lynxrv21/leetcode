"""
020_valid_parentheses.py
https://leetcode.com/problems/valid-parentheses/description/
#easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


def valid_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == "(":
            stack.append(")")
        elif char == "[":
            stack.append("]")
        elif char == "{":
            stack.append("}")
        elif not stack or stack.pop() != char:
            return False

    return not stack


def valid_parentheses_map(s: str) -> bool:
    p_map = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    p_stack = []

    for char in s:
        if char in p_map:
            if not p_stack or p_stack.pop() != p_map[char]:
                return False
        else:
            p_stack.append(char)

    return False if p_stack else True


if __name__ == "__main__":
    result = valid_parentheses("()[]{}")
    assert result is True, result

    result = valid_parentheses("(]")
    assert result is False, result
