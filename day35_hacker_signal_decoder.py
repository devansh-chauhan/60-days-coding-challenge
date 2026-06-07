def longest_unique_signal(signal):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(signal)):

        while signal[right] in seen:
            seen.remove(signal[left])
            left += 1

        seen.add(signal[right])
        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length


signal = "abcabcbb"
print("Signal:", signal)
result = longest_unique_signal(signal)
print("Longest Unique Signal Length:", result)