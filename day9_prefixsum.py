arr = [2, 4, 6, 8, 10]
prefix_sum = [0] * len(arr)
prefix_sum[0] = arr[0]

for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

print("Original Array:", arr)
print("Prefix Sum Array:", prefix_sum)

# Brute Force Approach
# Time Complexity: O(n)

def brute_force_sum(left, right):

    total = 0

    for i in range(left, right + 1):
        total += arr[i]

    return total

# Optimized Prefix Sum Approach
# Time Complexity: O(1)

def range_sum(left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left - 1]

queries = [(0, 2), (1, 3), (2, 4)]

print("\nRange Sum Queries:")

for l, r in queries:
    print(f"Query ({l}, {r})")

    print("Brute Force Result :", brute_force_sum(l, r))
    print("Optimized Result   :", range_sum(l, r))

    print()