def evaluate_rpn(tokens):
    stack = []
    for token in tokens:

        if token in ["+", "-", "*", "/"]:

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            elif token == "/":

                stack.append(int(a / b))

        else:
            stack.append(int(token))

    return stack[0]

test_cases = [
    ["2", "1", "+", "3", "*"],    
    ["4", "13", "5", "/", "+"],    
    ["10", "6", "9", "3", "+", "-11", "*",
     "/", "*", "17", "+", "5", "+"]
]

print("RPN Evaluation Results:\n")

for expression in test_cases:

    result = evaluate_rpn(expression)

    print(f"Expression: {expression}")
    print(f"Result: {result}\n")