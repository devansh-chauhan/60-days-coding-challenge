import time
def min_cost_recursive(cost, n):
    if n <= 1:
        return 0

    return min(
        min_cost_recursive(cost, n - 1) + cost[n - 1],
        min_cost_recursive(cost, n - 2) + cost[n - 2]
    )

def min_cost_dp(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(
            dp[i - 1] + cost[i - 1],
            dp[i - 2] + cost[i - 2]
        )
    return dp[n]

cost = [10, 15, 20]
start = time.time()
recursive_result = min_cost_recursive(cost, len(cost))
recursive_time = time.time() - start

start = time.time()
dp_result = min_cost_dp(cost)
dp_time = time.time() - start

print("Cost Array:", cost)

print("\nRecursive Result:", recursive_result)
print("Recursive Time:", recursive_time)

print("\nDP Result:", dp_result)
print("DP Time:", dp_time)