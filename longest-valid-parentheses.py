def longest_valid_parentheses(s):
    stack = [-1]
    answer = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                answer = max(answer, i - stack[-1])

    return answer


if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print("Longest Valid Parentheses Length:", longest_valid_parentheses(s))
