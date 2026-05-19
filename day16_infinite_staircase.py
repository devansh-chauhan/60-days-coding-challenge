import time

# Recursive Solution
# Time Complexity: O(2^n)

def climb_recursive(n):

    if n == 0 or n == 1:
        return 1

    return climb_recursive(n - 1) + climb_recursive(n - 2)


# Optimized Solution using Memoization
# Time Complexity: O(n)

memo = {}

def climb_memoization(n):

    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = (
        climb_memoization(n - 1)
        + climb_memoization(n - 2)
    )

    return memo[n]


n = 35
start = time.time()
recursive_result = climb_recursive(n)
end = time.time()

print("Recursive Solution:")
print("Ways to climb:", recursive_result)
print("Execution Time:", end - start, "seconds")

start = time.time()
memo_result = climb_memoization(n)
end = time.time()

print("\nOptimized Memoization Solution:")
print("Ways to climb:", memo_result)
print("Execution Time:", end - start, "seconds")