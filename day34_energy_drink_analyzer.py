import time

# Naive Solution

def max_average_naive(nums, k):

    max_avg = float('-inf')

    for i in range(len(nums) - k + 1):

        window_sum = 0

        for j in range(i, i + k):
            window_sum += nums[j]

        avg = window_sum / k

        max_avg = max(max_avg, avg)

    return max_avg

# Sliding Window Solution

def max_average_sliding_window(nums, k):

    window_sum = sum(nums[:k])

    max_sum = window_sum

    for i in range(k, len(nums)):

        window_sum += nums[i]
        window_sum -= nums[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum / k

energy = [1, 12, -5, -6, 50, 3]

k = 4

# Naive Approach
start = time.time()
naive_result = max_average_naive(energy, k)
end = time.time()

print("Naive Maximum Average:", naive_result)
print("Execution Time:", end - start)

# Sliding Window Approach
start = time.time()
optimized_result = max_average_sliding_window(energy, k)
end = time.time()

print("\nSliding Window Maximum Average:", optimized_result)
print("Execution Time:", end - start)