# Recursion Problem: Factorial Without Built-in Functions

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Stack Problem: Reverse String Using Stack
# Without Built-in reverse helpers

def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""

    while len(stack) > 0:
        reversed_text += stack.pop()

    return reversed_text

number = 5

print("Factorial Calculation:")
print(f"Factorial of {number} =", factorial(number))

print("\nString Reversal Using Stack:")

text = "ENGINEER"

print("Original String :", text)

print("Reversed String :", reverse_string(text))