import time

# Brute Force Solution
# Time Complexity: O(n²)
def max_water_bruteforce(height):
    maximum = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            area = min(height[i], height[j]) * width
            maximum = max(maximum, area)

    return maximum


# Optimized Two Pointer Solution
# Time Complexity: O(n)
def max_water_optimized(height):
    left = 0
    right = len(height) - 1
    maximum = 0
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        maximum = max(maximum, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


walls = [1, 8, 6, 2, 5, 4, 8, 3, 7]

start = time.time()
brute_result = max_water_bruteforce(walls)
end = time.time()
print("Brute Force Result:", brute_result)
print("Execution Time:", end - start)


start = time.time()
optimized_result = max_water_optimized(walls)
end = time.time()
print("\nOptimized Result:", optimized_result)
print("Execution Time:", end - start)