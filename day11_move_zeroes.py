def move_zeroes(arr):
    left = 0

    for right in range(len(arr)):

        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr

nums = [0, 1, 0, 3, 12]

print("Original Array:", nums)
result = move_zeroes(nums)
print("Updated Array :", result)