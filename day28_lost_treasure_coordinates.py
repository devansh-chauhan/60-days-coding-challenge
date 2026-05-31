import time

# Brute Force Solution
# Time Complexity: O(n²)

def two_sum_brute(nums, target):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:

                return [i, j]

    return []


# Optimized Solution Using Hashing
# Time Complexity: O(n)

def two_sum_optimized(nums, target):

    seen = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in seen:

            return [seen[complement], i]

        seen[nums[i]] = i

    return []


coordinates = [2, 7, 11, 15]

target = 9

# Brute Force Timing
start = time.time()

brute_result = two_sum_brute(
    coordinates,
    target
)

end = time.time()

print("Brute Force Result:", brute_result)
print("Execution Time:", end - start)

# Optimized Timing
start = time.time()

optimized_result = two_sum_optimized(
    coordinates,
    target
)

end = time.time()

print("\nOptimized Result:", optimized_result)
print("Execution Time:", end - start)