def is_balanced(sequence):
    stack = []

    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in sequence:

        if char in "({[":
            stack.append(char)

        elif char in ")}]":

            if not stack:
                return False

            top = stack.pop()

            if top != brackets[char]:
                return False

    return len(stack) == 0

test_cases = [
    "{[()]}",
    "((()))",
    "{[(])}",
    "([)]",
    "{[}",
    ""
]

print("Bracket Validation Results:\n")

for sequence in test_cases:

    result = is_balanced(sequence)

    print(f"{sequence} -> {result}")