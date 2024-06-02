# leetcode

This repository contains my solutions to some of the problems from [LeetCode](https://leetcode.com/). 
The solutions are organized by problem categories.

## Table of Contents

- [How to Use](#how-to-use)
- [Directory Structure](#directory-structure)
- [Problem List](#problem-list)
- [Resources](#resources)
- [Contributing](#contributing)

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/LeetCodeSolutions.git
   ```
2. Get random problem to solve:
   ```sh
   python generate_problem.py
   ```
   Optionally, specify complexity:
   ```sh
   python generate_problem.py [easy, medium]
   ```
3. New template file will be generated, with problem description and test cases

## Directory Structure

```plaintext
leetcode/
├── arrays
│   ├── 001_two_sum.py
│   ├── 121_best_time_to_buy_and_sell_stock.py
│   ├── 217_contains_duplicate.py
│   └── 242_valid_anagram.py
├── linked_lists
│   ├── 002_add_two_numbers.py
│   ├── 021_merge_two_sorted_lists.py
│   ├── 206_reverse_linked_list.py
│   └── utils.py
├── stack
│   └── 020_valid_parentheses.py
├── trees
│   ├── 104_maximum_depth_of_binary_tree.py
│   ├── 226_invert_binary_tree.py
│   └── utils.py
├── two_pointers
│   └── 020_valid_parentheses.py
├── get_problem.py
└── README.md
```

## Problem List

### Arrays
- [001_two_sum.py](arrays/001_two_sum.py)
- 053_maximum_subarray.py
- [121_best_time_to_buy_and_sell_stock.py](arrays/121_best_time_to_buy_and_sell_stock.py)
- [217_contains_duplicate.py](arrays/217_contains_duplicate.py)
- [242_valid_anagram.py](arrays/242_valid_anagram.py)
### Linked Lists
- [002_add_two_numbers.py](linked_lists/002_add_two_numbers.py)
- [021_merge_two_sorted_lists.py](linked_lists/021_merge_two_sorted_lists.py)
- [206_reverse_linked_list.py](linked_lists/206_reverse_linked_list.py)
- 141_linked_list_cycle.py
### Stack
- [020_valid_parentheses](stack/020_valid_parentheses.py)
### Trees
- 102_binary_tree_level_order_traversal.py
- [104_maximum_depth_of_binary_tree.py](trees/104_maximum_depth_of_binary_tree.py)
- [226_invert_binary_tree.py](trees/226_invert_binary_tree.py)
### Two Pointers
- [125_valid_palindrome.py](two_pointers/125_valid_palindrome.py)
### Dynamic Programming
- 070_climbing_stairs.py
- 198_house_robber.py
- 300_longest_increasing_subsequence.py

## Resources

[NeetCode](https://leetcode.io/) - coding challenges and some courses

[System Design Primer](https://github.com/donnemartin/system-design-primer) - Guide to system design interviews

[TechDummies](https://www.youtube.com/@TechDummiesNarendraL/playlists) - System design video guides

[gkcs](https://www.youtube.com/@gkcs) - Another system design and algorithms YT channel

Grokking the System Design Interview - Online course (paid)

## Contributing

Contributions are welcome! If you have solutions or improvements to existing ones, feel free to submit a pull request.
Please check the code before submitting:
```sh
python run_tests.py
black .
ruff check .
```