def is_valid(s):
    stack = []

    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in mapping.values():
            stack.append(ch)

        elif ch in mapping:

            if not stack or stack.pop() != mapping[ch]:
                return False

        else:
            return False

    return len(stack) == 0

tests = [
    "()",
    "()[]{}",
    "(]",
    "([{}])",
    "((("
]

print("=== DSA Challenge ===")
for t in tests:
    print(f"{t} -> {is_valid(t)}")


def find_max(numbers):
    if not numbers:
        return None

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


print("\n=== Debugging Challenge ===")
arr = [4, 9, 2, 18, 7]
print("Maximum:", find_max(arr))

print("\n=== System Design Scenario ===")
print("""
Design: URL Shortener

Components:
1. User sends long URL.
2. Server generates unique short code.
3. Store mapping in database.
4. Redirect short URL to original URL.

Flow:

User
  |
  | Long URL
  v
Backend Server
  |
Generate Short Code
  |
Store Mapping
  |
Database
  |
Return Short URL

Future Improvements:
- Analytics
- Custom aliases
- Expiration dates
- Load balancing
- Caching
""")