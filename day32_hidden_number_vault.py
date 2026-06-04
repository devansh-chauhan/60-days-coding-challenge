import time
# Linear Search
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1

# Iterative Binary Search
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Sorted Vault
vault = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

target = 35

print("Vault:", vault)
print("Target Code:", target)

# Linear Search Timing
start = time.time()
linear_result = linear_search(vault, target)
end = time.time()

print("\nLinear Search Result:", linear_result)
print("Time:", end - start)

# Binary Search Timing
start = time.time()
binary_result = binary_search(vault, target)
end = time.time()

print("\nBinary Search Result:", binary_result)
print("Time:", end - start)