# Longest Valid Parentheses

## Problem
Given a string containing only '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

## Language
Python 3

## Algorithm
- Use a stack to store indices.
- Initialize the stack with -1.
- Push the index of every '('.
- For every ')':
  - Pop the stack.
  - If the stack becomes empty, push the current index.
  - Otherwise, calculate the current valid length.
- Keep track of the maximum length.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Run

```bash
python longest_valid_parentheses.py
```

### Example

Input

```
)()())
```

Output

```
4
```
