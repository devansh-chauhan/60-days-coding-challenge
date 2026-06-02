# Problem 2: Container With Most Water
def max_water(height):

    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:

        width = right - left

        current_area = min(
            height[left],
            height[right]
        ) * width

        maximum = max(
            maximum,
            current_area
        )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


heights = [1,8,6,2,5,4,8,3,7]

print("Maximum Water:", max_water(heights))